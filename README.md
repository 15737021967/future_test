使用说明

因为是将配置写在环境变量中，所以再本地需要先创建一个.env文件
```text
# 运行环境
ENV=local


# FLASK配置
APP_HOST=0.0.0.0
APP_PORT=8080

# SQLALCHEMY配置信息
SQLALCHEMY_DATABASE_URI=mysql+pymysql://root:gllue123@localhost/blog
SQLALCHEMY_RECORD_QUERIES=1
SQLALCHEMY_TRACK_MODIFICATIONS=0
SQLALCHEMY_UNITTEST_DATABASE_URI=mysql+pymysql://root:gllue123@localhost/blog
SQLALCHEMY_POOL_SIZE=10
SQLALCHEMY_POOL_RECYCLE=3600
SQLALCHEMY_ECHO=1

# REDIS配置
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=1
REDIS_PASSWORD=
```
export FLASK_APP=blog

运行项目
flask run
生成migrations文件
flask db migrate
执行迁移脚本
flask db upgrade
运行shell脚本
flask shell
