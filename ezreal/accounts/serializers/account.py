from marshmallow import Schema, fields, ValidationError


class SignInSerializer(Schema):
    account = fields.String(required=True)
    password = fields.String(required=True)
    remember_me = fields.Boolean(default=False)
