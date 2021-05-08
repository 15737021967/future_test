import json

from marshmallow import ValidationError

from ezreal.accounts.exceptions import AuthError
from ezreal.accounts.serializers.account import SignInSerializer, EmailSignUpSerializer
from ezreal.accounts.services.accounts import AccountsService
from flask import request

from ezreal.common.exceptions import ParamsRequiredError
from ezreal.common.response import standard_response_with_data, standard_exception_response

from flask import Blueprint

accounts_api = Blueprint('accounts', __name__)


@accounts_api.route('/sign-in/', methods=['POST'])
def sign_in():
    try:
        serializer = SignInSerializer().load(json.loads(request.get_data()))
        result = AccountsService.sign_in(**serializer)
    except ValidationError:
        return standard_exception_response(ParamsRequiredError)

    except AuthError as e:
        return standard_exception_response(e)

    return standard_response_with_data(result)


@accounts_api.route('/sign-up/', methods=['POST'])
def sign_up():
    try:
        serializer = EmailSignUpSerializer().load(json.loads(request.get_data()))
        user_id = AccountsService.sign_up(serializer['email'], serializer['password'], serializer['verify_code'])
    except ValidationError:
        return standard_exception_response(ParamsRequiredError)

    return standard_response_with_data({'user_id': user_id})
