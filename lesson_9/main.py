from flask import Flask, request, jsonify
import json

app = Flask(__name__)

users_data = {
    '1': {
        'username': 'MAgnus',
        'email': 'magnus@gmail.com',
        'data': {
            'Age': 22,
            'interest': 'football'
        }
    },
    '2': {
        'username': 'Sendy',
        'email': 'sendy@gmail.com',
        'data': {
            'Age': 24,
            'interest': 'music'
        }
    }
}


@app.route('/users', methods=['GET', 'POST'])
@app.route('/users/<string:user_id>', methods=['GET', 'PUT', 'DELETE'])
def users(user_id=None):
    if request.method == 'GET':
        data = users_data
        if user_id:
            data = data.get(user_id)
        return jsonify(data)

    elif request.method == 'POST':
        users_data.update(**request.json)
        return jsonify(request.json)

    elif request.method == 'PUT':
        users_data[user_id].update(request.json)
        return jsonify(users_data[user_id])

    elif request.method == 'DELETE':
        del users_data[user_id]
        return users_data











# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'GET':
#         return render_template('index.html')
#     elif request.method == 'POST':
#         print(request.form['surname'])
#         return 'Hello world'


app.run(debug=True)