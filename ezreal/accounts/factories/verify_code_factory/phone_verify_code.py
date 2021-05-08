from ezreal.accounts.factories.verify_code_factory.base import BaseVerifyCodeService


class PhoneVerifyCodeService(BaseVerifyCodeService):

    @classmethod
    def _send_verify_code(cls, receiver: str, verify_code: str, scene: int):
        pass

    @classmethod
    def _get_cache_key(cls, receiver: str, verify_code: str, scene: int):
        pass
