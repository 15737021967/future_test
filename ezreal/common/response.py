from flask import jsonify

from ezreal.expections import EzRealException


def standard_ok_response():
    response_data = {
        'code': 200,
        'success': True,
        'detail': None,
    }
    return jsonify(response_data), 200


def standard_response_with_data(data=None):
    response_data = {
        'data': data,
        'code': 200,
        'success': True
    }

    return jsonify(response_data), 200


def standard_error_response(code=None, message=None):
    response_data = {
        'message': message,
        'code': code,
        'success': False
    }
    return jsonify(response_data), 200


def standard_exception_response(error: EzRealException):
    response_data = {
        'code': error.code,
        'message': error.message,
        'success': False
    }

    return jsonify(response_data), 200
