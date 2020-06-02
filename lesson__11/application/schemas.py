from marshmallow import Schema, fields, validates, ValidationError


class CarSchema(Schema):
    model = fields.String()
    engine = fields.String()


class UserSchema(Schema):
    id = fields.String(dump_only=True)
    login = fields.String(required=True)
    password = fields.String(required=True, load_only=True)
    car = fields.Nested(CarSchema, dump_only=True)
    interests = fields.List(fields.String)

    @validates('password')
    def validate(self, value):
        if all([value.isalnum(), len(value) > 8]):
            return value
        else:
            raise ValidationError(message={'Error': 'Not valid pass'})
