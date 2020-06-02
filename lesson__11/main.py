from flask import Flask
from flask_restful import Api
from application.resources import UserResource

app = Flask(__name__)
api = Api(app)

api.add_resource(UserResource, '/user')

app.run(debug=True)

