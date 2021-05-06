

class EzRealException(Exception):
    message = ""
    code = ""

    def __init__(self, message: str = None):
        self.message = message or self.message


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
