from feature import db
from sqlalchemy import func, text


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    added_time = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now())
    update_time = db.Column(
        db.TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )
