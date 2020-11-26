from flask import Blueprint

sentry_api = Blueprint(
    "sentry",
    __name__
)


from feature.sentry.models import *
from feature.sentry.views import *
