from ezreal import db
from ezreal.accounts.exceptions import AuthError, EmailHasBeenRegistered, VerifyCodeError
from ezreal.accounts.factories import VerifyCodeFactory
from ezreal.accounts.models import User, UserProfile
from ezreal.common import service
from ezreal.ez_jwt.tokens import RefreshToken
from ezreal.accounts.utils import pbkdf2_password_hasher, get_random_string
from ezreal.utils import lock_by_key


class AccountsService(service.BaseService):

    @classmethod
    def sign_in(cls, account=None, password=None, remember_me=False):
        if '@' in account:
            user = db.session.query(User).filter(
                User.email == account
            ).first()
        else:
            user = db.session.query(User).filter(
                User.phone == account
            ).first()
        if user is None or not user.check_password(password):
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
    def sign_up(cls, email: str, password: str, verify_code: str):
        success = cls.check_verify_code(account=email, verify_code=verify_code, scene=1)
        if not success:
            raise VerifyCodeError

        user = db.session.query(User).filter(User.email == email).first()
        if user:
            raise EmailHasBeenRegistered

        salt = pbkdf2_password_hasher.salt()
        with lock_by_key(f'sign_up_by_email:{email}'):
            user = User(
                email=email,
                password=pbkdf2_password_hasher.encode(password=password, salt=salt),
                salt=salt,
            )
            user_profile = UserProfile(
                user=user,
                nickname=cls.make_default_nickname(),
            )
            db.session.add_all([user, user_profile])
            db.session.commit()

        return user.id

    @classmethod
    def make_default_nickname(cls):
        return f'Hello_{get_random_string(6).upper()}'

    @classmethod
    def send_verify_code(cls, account: str, verify_code: str, scene: int):
        factory = VerifyCodeFactory.get(account)
        return factory.check_verify_code(receiver=account, verify_code=verify_code, scene=scene)

    @classmethod
    def check_verify_code(cls, account: str, verify_code: str, scene: int):
        factory = VerifyCodeFactory.get(account)
        return factory.check_verify_code(receiver=account, verify_code=verify_code, scene=scene)
