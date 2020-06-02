from flask_restful import Resource
from .models import User
from flask import request
from .schemas import UserSchema
import json
from marshmallow import ValidationError


class UserResource(Resource):

    def get(self):
        users = User.objects.all()
        json_obj = UserSchema(many=True).dumps(users)
        return json.loads(json_obj)

    def post(self):

        json_data = json.dumps(request.json)
        try:
            res = UserSchema().loads(json_data)
            res = json.loads(UserSchema().dumps(res))
        except ValidationError as err:
            res = err.messages
        return res