import sentry_sdk

from ezreal.config import config
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sentry_sdk.integrations.flask import FlaskIntegration


app = Flask(__name__)
app.config.from_object(config)


@app.route('/health/')
def health():
    return jsonify('ok')


sentry_sdk.init(
    dsn=app.config.get("SENTRY_DSN"),
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)

TESTING = app.config.get("TESTING")

if not TESTING:
    db = SQLAlchemy(app=app)
    migrate = Migrate(app, db)

else:
    # 单元测试使用测试的db
    from ezreal import tests
    db = tests.db

# 加载中间件
from ezreal.middleware import *

# 加载脚本
from ezreal.command import *

# 注册相关路由
from ezreal.accounts.api import accounts_api


router_list = [
    accounts_api
]

for api in router_list:
    app.register_blueprint(api, url_prefix=f"/v1/api/{api.name}")
