from ezreal import db
from ezreal.common.models import BaseModel


class User(BaseModel):

    email = db.Column(db.String(64), verbose_name="邮箱", nullable=True)
    country_code = db.Column(db.String(126), null=True, blank=True, )
    phone = db.Column(db.Integer, verbose_name="手机号码", nullable=True)
    password = db.Column(db.String(128), verbose_name="密码", nullable=False)
    salt = db.Column(db.String(128), nullable=False)
    is_superuser = db.Column(db.Boolean, server_default=False, verbose_name="超级管理员")
    is_staff = db.Column(db.Boolean, server_default=False, verbose_name="是否是职员")
    is_active = db.Column(db.Boolean, server_default=False, verbose_name="活跃用户")
    date_joined = db.Column(db.TIMESTAMP, null=True, verbose_name="注册时间")
    last_login_datetime = db.Column(db.TIMESTAMP, null=True, verbose_name="上一次登录时间")
    last_login_ip = db.Column(db.String(32), nullable=True, verbose_name="上一次登录IP")


class UserProfile(BaseModel):

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    nickname = db.Column(db.String(64), nullable=False, verbose_name="昵称")
    introduction = db.Column(db.Text, verbose_name="个人介绍")

    @property
    def user_instance(self):
        return db.session.query(User).filter(id=self.user_id).first()
