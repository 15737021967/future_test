from ezreal.expections import BuildException


class AccountBuildException(BuildException):
    exception_code = 'A'
    exception_number = 10000


UserProfileError = AccountBuildException.build(
    exception_name="UserProfileHasNotUserError",
    exception_code=AccountBuildException.exception_code+str(AccountBuildException.exception_number+1).zfill(4),
    exception_message="The userprofile has not bind user error"
)
