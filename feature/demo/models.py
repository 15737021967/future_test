from feature.common.models import BaseModel
from feature import db


class DemoModel(BaseModel):
    name = db.Column(db.String(256), nullable=False, server_default="")
    age = db.Column(db.Integer, nullable=False, server_default=db.text('-1'))
    sex = db.Column(db.SMALLINT, nullable=False, server_default=db.text('-1'))
