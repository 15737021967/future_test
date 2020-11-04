from flask import Blueprint

article_api = Blueprint(
    'article',
    __name__
)

from blog.article import views
from blog.article import models
