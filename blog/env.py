import os
import dotenv

dotenv.load_dotenv(verbose=True)

# 运行环境
ENV = os.environ.get("ENV")
TESTING = int(os.environ.get("TESTING", 0))

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
