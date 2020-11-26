import sentry_sdk

from feature import env
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sentry_sdk.integrations.flask import FlaskIntegration


sentry_sdk.init(
    dsn=env.SENTRY_DSN,
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)

app = Flask(__name__)

# 初始化数据库连接
app.config["SQLALCHEMY_DATABASE_URI"] = env.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_RECORD_QUERIES"] = env.SQLALCHEMY_RECORD_QUERIES
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = env.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_size': env.SQLALCHEMY_POOL_SIZE, 'pool_recycle': env.SQLALCHEMY_POOL_RECYCLE
}
app.config["SQLALCHEMY_ECHO"] = env.SQLALCHEMY_ECHO

TESTING = env.TESTING

if not TESTING:
    db = SQLAlchemy(app=app)
    migrate = Migrate(app, db)

else:
    # 单元测试使用测试的db
    from feature import tests
    db = tests.db

# 加载中间件
from feature.common.middleware import *

# 注册相关路由
from feature.article import article_api
from feature.sentry import sentry_api

app.register_blueprint(article_api, url_prefix="/api/v1/feature")
app.register_blueprint(sentry_api, url_prefix="/api/v1/sentry")
