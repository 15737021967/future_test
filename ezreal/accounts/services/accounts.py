from ezreal import db
from ezreal.accounts.exceptions import AuthError, EmailHasBeenRegistered
from ezreal.common import service
from ezreal.accounts.models import User
from ezreal.ez_jwt.tokens import RefreshToken


class AccountsService(service.BaseService):

    @classmethod
    def sign_in(cls, account=None, password=None, remember_me=False):
        if '@' in account:
            user = db.session.query(User).filter(
                User.email == account,
                User.password == password
            ).first()
        else:
            user = db.session.query(User).filter(
                User.phone == account,
                User.password == password
            ).first()
        if user is None:
            raise AuthError
        return cls.auth_for_user(user)

    @classmethod
    def auth_for_user(cls, user):
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token
        return {
            'refresh': str(refresh),
            'access': str(access),
            'access_exp': access.payload['exp'],
            'access_lifetime': int(access.lifetime.total_seconds())
        }

    @classmethod
    def sign_up(cls, email: str, password: str):
        user = db.session.query(User).filter(User.email == email).first()
        if user:
            raise EmailHasBeenRegistered
