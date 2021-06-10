import json

from flask import request
from werkzeug.exceptions import HTTPException


class EzRealException(Exception):
    message = ""
    code = ""

    def __init__(self, message: str = None, code: str = None):
        self.message = message or self.message
        self.code = self.code or code


class BuildException:

    exception_code = None
    exception_number = -1

    @classmethod
    def build(cls, exception_name: str, exception_code: str, exception_message: str):
        if cls.exception_number is None or cls.exception_number == -1:
            raise EzRealException(
                message=f"{cls.__name__}: Variable is not rewritten exception", code="A0000"
            )
        return type(
            exception_name,
            (EzRealException,),
            {
                "code": exception_code,
                "message": exception_message
            }
        )


class APIException(HTTPException):
    code = 200
    message = 'sorry, we made a mistake!'
    error_code = 'A0001'

    def __init__(self, message=None, code=None, error_code: EzRealException = None):
        if code:
            self.code = code
        if message:
            self.message = message
        if error_code:
            self.error_code = error_code.code
            self.msg = error_code.message

        super(APIException, self).__init__(message, None)

    def get_body(self, environ=None):
        body = dict(
            message=self.message,
            code=self.error_code,
            success=False,
            data=None,
            request=request.method + ' ' + self.get_url_no_param(),
        )
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]
