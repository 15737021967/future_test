from flask import Blueprint

sentry_api = Blueprint(
    "sentry",
    __name__
)


from blog.sentry.models import *
from blog.sentry.views import *
