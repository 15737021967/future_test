from sqlalchemy.orm import backref

from ezreal import db
from ezreal.accounts.utils import pbkdf2_password_hasher
from ezreal.common.models import BaseModel


class User(BaseModel):

    email = db.Column(db.String(64), doc="邮箱", nullable=True, unique=True)
    country_code = db.Column(db.String(126), nullable=True)
    phone = db.Column(db.Integer, doc="手机号码", nullable=True, unique=True)
    password = db.Column(db.String(128), doc="密码", nullable=False)
    salt = db.Column(db.String(128), nullable=False)
    is_superuser = db.Column(db.Boolean, default=False, doc="超级管理员")
    is_staff = db.Column(db.Boolean, default=False, doc="是否是职员")
    is_active = db.Column(db.Boolean, default=True, doc="活跃用户")
    last_login_datetime = db.Column(db.TIMESTAMP, nullable=True, doc="上一次登录时间")
    last_login_ip = db.Column(db.String(32), nullable=True, doc="上一次登录IP")

    def check_password(self, password: str):
        return pbkdf2_password_hasher.verify(password, self.password)


class UserProfile(BaseModel):

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), unique=True)
    nickname = db.Column(db.String(64), nullable=False, doc="昵称")
    introduction = db.Column(db.Text, doc="个人介绍", default="还没有填写个人介绍")
    user = db.relationship('User', backref=backref('profile', lazy='joined'), lazy='joined')
