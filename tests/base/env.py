import uuid

from tests.base.base import BaseEnv, SampleData
from functools import wraps
from flask import g
from unittest import mock
from tests.sample_data import user


def with_env(env: BaseEnv, login_user: SampleData = user.anonymous_user):
    env.sample_data_list.append(login_user)

    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with env:
                # from app import load_user_from_request
                # load_user_from_request = mock.Mock(return_value=login_user.instance)
                g.user = login_user.instance
                g.token = uuid.uuid4()
                func(*args, **kwargs)
        return wrapper
    return decorate
