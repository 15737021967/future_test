import datetime

from uuid import uuid4
from ezreal.config import config
from ezreal.ez_jwt import exceptions
from ezreal.ez_jwt import utils
from ezreal.ez_jwt.backends import token_backend


class Token:

    token_type = None
    lifetime = None

    def __init__(self, token=None, verify=True):

        if self.token_type is None or self.lifetime is None:
            raise exceptions.TokenError("Cannot create token with no type or lifetime")

        self.token = token
        self.current_time = datetime.datetime.utcnow()

        # Set up token
        if token is not None:
            # An encoded token was provided

            # Decode token
            try:
                self.payload = token_backend.decode(token, verify=verify)
            except exceptions.InvalidTokenError:
                raise exceptions.InvalidTokenError

            if verify:
                self.verify()
        else:
            # New token.  Skip all the verification steps.
            self.payload = {config.JWT_TOKEN_TYPE_CLAIM: self.token_type}

            # Set "exp" claim with default value
            self.set_exp(from_time=self.current_time, lifetime=self.lifetime)

            # Set "jti" claim
            self.set_jti()

    def __repr__(self):
        return repr(self.payload)

    def __getitem__(self, key):
        return self.payload[key]

    def __setitem__(self, key, value):
        self.payload[key] = value

    def __delitem__(self, key):
        del self.payload[key]

    def __contains__(self, key):
        return key in self.payload

    def get(self, key, default=None):
        return self.payload.get(key, default)

    def __str__(self):

        return token_backend.encode(self.payload)

    def verify(self):

        self.check_exp()

        # Ensure token id is present
        if config.JWT_JTI_CLAIM not in self.payload:
            raise exceptions.TokenError("Token has no id")

        self.verify_token_type()

    def verify_token_type(self):
        """
        Ensures that the token type claim is present and has the correct value.
        """
        try:
            token_type = self.payload[config.JWT_TOKEN_TYPE_CLAIM]
        except KeyError:
            raise exceptions.TokenError("Token has no type")

        if self.token_type != token_type:
            raise exceptions.TokenError("Token has wrong type")

    def set_jti(self):

        self.payload[config.JTI_CLAIM] = uuid4().hex

    def set_exp(self, claim='exp', from_time=None, lifetime=None):
        """
        Updates the expiration time of a token.
        """
        if from_time is None:
            from_time = self.current_time

        if lifetime is None:
            lifetime = self.lifetime

        self.payload[claim] = utils.datetime_to_epoch(from_time + lifetime)

    def check_exp(self, claim='exp', current_time=None):
        """
        Checks whether a timestamp value in the given claim has passed (since
        the given datetime value in `current_time`).  Raises a TokenError with
        a user-facing error message if so.
        """
        if current_time is None:
            current_time = self.current_time

        try:
            claim_value = self.payload[claim]
        except KeyError:
            raise exceptions.TokenError(f"Token has no '{claim}' claim")

        claim_time = utils.datetime_from_epoch(claim_value)
        if claim_time <= current_time:
            raise exceptions.TokenError(f"Token '{claim}' claim has expired")


class AccessToken(Token):
    token_type = 'access'
    lifetime = datetime.timedelta(seconds=config.JWT_ACCESS_TOKEN_LIFETIME)


class RefreshToken(Token):
    token_type = 'refresh'
    lifetime = config.JWT_REFRESH_TOKEN_LIFETIME
    no_copy_claims = (
        config.JWT_TOKEN_TYPE_CLAIM,
        'exp',
        config.JWT_JTI_CLAIM,
        'jti',
    )

    @property
    def access_token(self):
        """
        Returns an access token created from this refresh token.  Copies all
        claims present in this refresh token to the new access token except
        those claims listed in the `no_copy_claims` attribute.
        """
        access = AccessToken()
        access.set_exp(from_time=self.current_time)

        no_copy = self.no_copy_claims
        for claim, value in self.payload.items():
            if claim in no_copy:
                continue
            access[claim] = value

        return access

