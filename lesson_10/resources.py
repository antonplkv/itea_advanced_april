from flask_restful import Resource
from models import Cars
from flask import jsonify, request


class CarResource(Resource):

    def get(self):
        return Cars.objects.to_json()

    def post(self):
        result = Cars.objects.create(**request.json)
        return result.to_json()

    def put(self):
        print('PUT')

    def delete(self):
        print('DELETE')