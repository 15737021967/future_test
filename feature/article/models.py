from feature import db
from feature.common.models import BaseModel


article_tag_table = db.Table(
    "article_tag",
    db.Column("article_id", db.Integer, db.ForeignKey("article.id")),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"))
)


class Article(BaseModel):
    title = db.Column(db.String(526), nullable=True)
    describe = db.Column(db.Text, nullable=True)
    content = db.Column(db.Text, nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    tags = db.relationship("Tag", secondary=article_tag_table, backref="articles", lazy="dynamic")


class Category(BaseModel):

    name = db.Column(db.String(512), nullable=True)
    articles = db.relationship("Article", backref="category", lazy="dynamic")


class Tag(BaseModel):

    name = db.Column(db.String(512), nullable=True)
