from flask import Blueprint

article_api = Blueprint(
    'article',
    __name__
)

from ezreal.article import views
from ezreal.article import models
