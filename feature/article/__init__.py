from flask import Blueprint

article_api = Blueprint(
    'article',
    __name__
)

from feature.article import views
from feature.article import models
