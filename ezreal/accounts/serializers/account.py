from marshmallow import Schema, fields, ValidationError, validates_schema


class SignInSerializer(Schema):
    account = fields.String(required=True)
    password = fields.String(required=True)
    remember_me = fields.Boolean(default=False)


class SignUpSerializer(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)
    confirm_password = fields.String(required=True)

    @validates_schema
    def validate_confirm_password(self, data, **kwargs):
        if data['password'] != data['confirm_password']:
            raise ValidationError('confirm password error.')
