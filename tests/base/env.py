from tests.base.base import BaseEnv
from tests.sample_data import jwt_to_user
from functools import wraps


def with_env(env: BaseEnv):
    """
    构建测试样例
    """
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with env:
                func(*args, **kwargs)
        return wrapper
    return decorate


def with_jwt(jwt: jwt_to_user.JwtToUserId):
    """
    通过jwt构建登录状态，强系统相关，需要根据具体情况作出修改
    """
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with jwt:
                func(*args, **kwargs)
        return wrapper
    return decorate
