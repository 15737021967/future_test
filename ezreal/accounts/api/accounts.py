import json

from ezreal.accounts.serializers.account import SignInSerializer
from ezreal.accounts.services import accounts as accounts_service
from flask import request, g, jsonify

from flask import Blueprint

accounts_api = Blueprint(
    'accounts',
    __name__
)


@accounts_api.route('/sign_in/', methods=['POST'])
def sign_in():
    serializer = SignInSerializer().load(json.loads(request.get_data()))
    data = accounts_service.AccountsService
    return jsonify("ok")

