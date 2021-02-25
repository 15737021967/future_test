from tests.sample_data import user as user_data
from flask import g


class JwtToUserId:
    def __init__(self, jwt: str, user: user_data.User):
        self.jwt = jwt
        self.user = user

    def __enter__(self):
        g.user = self.user
        user_token = self.jwt.replace('Bearer', '').strip()
        g.token = user_token

    def __exit__(self, exc_type, exc_val, exc_tb):
        g.user = None
        g.token = None


jwt_to_user_1 = JwtToUserId(
    jwt="Bearer a5b5da03-e8e8-4bb7-a694-fb87b2a00a80",
    user=user_data.common_user_1
)


jwt_to_user_2 = JwtToUserId(
    jwt="Bearer 640b8489-cea9-47ee-8127-50dd769ffe51",
    user=user_data.common_user_2
)
