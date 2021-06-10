from flask import jsonify

from ezreal.expections import EzRealException


def standard_ok_response():
    response_data = {
        'code': 200,
        'data': None,
        'message': '',
        'success': True
    }
    return jsonify(response_data), 200


def standard_response_with_data(data=None):
    response_data = {
        'code': 200,
        'data': data,
        'success': True,
        'message': ''
    }

    return jsonify(response_data), 200


def standard_error_response(code=None, message=None):
    response_data = {
        'code': code,
        'data': None,
        'success': False,
        'message': message
    }
    return jsonify(response_data), 200


def standard_exception_response(error: EzRealException):
    response_data = {
        'code': error.code,
        'data': None,
        'success': False,
        'message': error.message
    }

    return jsonify(response_data), 200
