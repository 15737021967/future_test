from ezreal.expections import BuildException


class AccountBuildException(BuildException):
    exception_code = 'B'
    exception_number = 10000


UserProfileError = AccountBuildException.build(
    exception_name="UserProfileHasNotUserError",
    exception_code=AccountBuildException.exception_code+str(AccountBuildException.exception_number+1).zfill(4),
    exception_message="The userprofile has not bind user error"
)


AuthError = AccountBuildException.build(
    exception_name='AuthError',
    exception_code=AccountBuildException.exception_code+str(AccountBuildException.exception_number+2).zfill(4),
    exception_message='Your username or password is not correct'
)


EmailHasBeenRegistered = AccountBuildException.build(
    exception_name='UserHasBeenRegistered',
    exception_code=AccountBuildException.exception_code+str(AccountBuildException.exception_number+3).zfill(4),
    exception_message='Email has been registered'
)
