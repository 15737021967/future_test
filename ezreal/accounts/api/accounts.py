import json

from ezreal.accounts.services import accounts as accounts_service
from flask import request, g, jsonify

from flask import Blueprint

accounts_api = Blueprint(
    'accounts',
    __name__
)


@accounts_api.route('/sign_in/', methods=['POST'])
def sign_in():
    data = json.loads(request.get_data())
    accounts = data.get("accounts")
    password = data.get("password")
    data = accounts_service.AccountsService
    return jsonify("ok")

