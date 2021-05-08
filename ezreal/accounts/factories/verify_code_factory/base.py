import abc
from ezreal import config


class BaseVerifyCodeService(abc.ABC):

    @classmethod
    def send_verify_code(cls, receiver: str, verify_code: str, scene: int):
        pass

    @classmethod
    def check_verify_code(cls, receiver: str, verify_code: str, scene: int):
        if verify_code == config.SUPER_VERIFY_CODE:
            return True
        return False

    @classmethod
    def _send_verify_code(cls, receiver: str, verify_code: str, scene: int):
        raise NotImplementedError

    @classmethod
    def _get_cache_key(cls, receiver: str, verify_code: str, scene: int):
        raise NotImplementedError
