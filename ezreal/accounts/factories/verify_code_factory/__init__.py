from ezreal.accounts.factories.verify_code_factory.email_verify_code import EmailVerifyCodeService
from ezreal.accounts.factories.verify_code_factory.phone_verify_code import PhoneVerifyCodeService


class VerifyCodeFactory:

    @classmethod
    def get(cls, account):
        if '@' in account:
            return EmailVerifyCodeService
        else:
            return PhoneVerifyCodeService


