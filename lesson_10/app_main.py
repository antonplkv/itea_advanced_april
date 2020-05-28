#Resources - controllers
#Models - mongoengine collections
#router - defining routes (app_main)

from flask import Flask, url_for
from flask_restful import Api
from resources import *

app = Flask(__name__)
api = Api(app)

api.add_resource(
    CarResource,
    '/cars',
    '/cars/<id>'
)

if __name__ == '__main__':
    app.run(debug=True)