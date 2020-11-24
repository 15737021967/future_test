from blog.sentry import sentry_api
from flask import jsonify


@sentry_api.route("/test_sentry/", methods=["GET"])
def test_sentry():
    test_a = 1
    test_b = 0
    result = test_a / test_b
    return jsonify({"status": True, "data": result})
