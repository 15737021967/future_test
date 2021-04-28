import os
import dotenv

dotenv.load_dotenv(verbose=True)


class Config:

    # 运行环境
    ENV = os.environ.get("ENV")
    TESTING = int(os.environ.get("TESTING", 0))

    # JWT 配置
    JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM", 'HS256')
    JWT_SIGNING_KEY = os.environ.get("JWT_SIGNING_KEY")
    JWT_VERIFYING_KEY = os.environ.get("JWT_VERIFYING_KEY", "")
    JWT_AUDIENCE = os.environ.get("JWT_AUDIENCE", "")
    JWT_ISSUER = os.environ.get("JWT_ISSUER", "")

    # 单位-分钟
    JWT_ACCESS_TOKEN_LIFETIME = int(os.environ.get("JWT_ACCESS_TOKEN_LIFETIME", 5))
    # 单位-分钟
    JWT_REFRESH_TOKEN_LIFETIME = int(os.environ.get("JWT_REFRESH_TOKEN_LIFETIME", 60 * 24))
    JWT_ROTATE_REFRESH_TOKENS = bool(os.environ.get("JWT_ROTATE_REFRESH_TOKENS", 0))

    JWT_TOKEN_TYPE_CLAIM = os.environ.get("JWT_TOKEN_TYPE_CLAIM", "token_type")
    JWT_JTI_CLAIM = os.environ.get("JWT_JTI_CLAIM", "jti")

    # SQLALCHEMY配置信息
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_RECORD_QUERIES = bool(int(os.environ.get("SQLALCHEMY_RECORD_QUERIES")))
    SQLALCHEMY_TRACK_MODIFICATIONS = bool(int(os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")))
    SQLALCHEMY_UNITTEST_DATABASE_URI = os.environ.get("SQLALCHEMY_UNITTEST_DATABASE_URI")
    SQLALCHEMY_POOL_SIZE = int(os.environ.get("SQLALCHEMY_POOL_SIZE"))
    SQLALCHEMY_POOL_RECYCLE = int(os.environ.get("SQLALCHEMY_POOL_RECYCLE"))
    SQLALCHEMY_ECHO = bool(os.environ.get("SQLALCHEMY_ECHO"))

    # REDIS配置
    REDIS_HOST = os.environ.get("REDIS_HOST")
    REDIS_PORT = os.environ.get("REDIS_PORT")
    REDIS_DB = int(os.environ.get("REDIS_DB", "0"))
    REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")

    # SENTRY配置
    SENTRY_DSN = os.environ.get("SENTRY_DSN")


config = Config()
