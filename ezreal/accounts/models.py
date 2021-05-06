from ezreal import db
from ezreal.common.models import BaseModel


class User(BaseModel):

    email = db.Column(db.String(64), doc="邮箱", nullable=True)
    country_code = db.Column(db.String(126), nullable=True)
    phone = db.Column(db.Integer, doc="手机号码", nullable=True)
    password = db.Column(db.String(128), doc="密码", nullable=False)
    salt = db.Column(db.String(128), nullable=False)
    is_superuser = db.Column(db.Boolean, default=False, doc="超级管理员")
    is_staff = db.Column(db.Boolean, default=False, doc="是否是职员")
    is_active = db.Column(db.Boolean, default=False, doc="活跃用户")
    date_joined = db.Column(db.TIMESTAMP, nullable=True, doc="注册时间")
    last_login_datetime = db.Column(db.TIMESTAMP, nullable=True, doc="上一次登录时间")
    last_login_ip = db.Column(db.String(32), nullable=True, doc="上一次登录IP")


class UserProfile(BaseModel):

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), unique=True)
    nickname = db.Column(db.String(64), nullable=False, doc="昵称")
    introduction = db.Column(db.Text, doc="个人介绍")

    @property
    def user_instance(self):
        return db.session.query(User).filter(id=self.user_id).first()
