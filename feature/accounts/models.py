from feature import db
from feature.common.models import BaseModel


class User(BaseModel):

    nickname = db.Column(db.String(64), verbose_name="昵称")
    email = db.Column(db.String(64), verbose_name="邮箱")
    phone = db.Column(db.Integer, verbose_name="手机号码")
    password = db.Column(db.String(128), verbose_name="密码")
    profile = db.Column(db.ForeignKey, )


class UserProfile(BaseModel):

    pass
