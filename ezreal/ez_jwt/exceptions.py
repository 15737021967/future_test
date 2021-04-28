from ezreal.expections import BuildException


class TokenBuildException(BuildException):
    exception_code = 'Z'
    exception_number = 10000


TokenBackendError = TokenBuildException.build(
    exception_name="UnrecognizedAlgorithmError",
    exception_code=TokenBuildException.exception_code+str(TokenBuildException.exception_number+1).zfill(4),
    exception_message="TokenBackend error."
)


TokenError = TokenBuildException.build(
    exception_name="TokenError",
    exception_code=TokenBuildException.exception_code+str(TokenBuildException.exception_number+2).zfill(4),
    exception_message="Token error."
)


InvalidTokenError = TokenBuildException.build(
    exception_name="InvalidTokenError",
    exception_code=TokenBuildException.exception_code+str(TokenBuildException.exception_number+3).zfill(4),
    exception_message="Token is invalid or expired"
)
