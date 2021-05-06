from ezreal.expections import BuildException


class CommonBuildException(BuildException):
    exception_code = 'A'
    exception_number = 10000


ParamsRequiredError = CommonBuildException.build(
    exception_name='ParamsRequiredError',
    exception_code=CommonBuildException.exception_code+str(CommonBuildException.exception_number+1).zfill(4),
    exception_message="params required error."
)



