from flask import Flask, jsonify, url_for, redirect
from blueprints import users_blueprint

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('users.get_users'))
    return jsonify({
        'message': 'Hello World'
    }), 400

@app.route('/hello-world', methods=['GET', 'POST'])
def hello_world():
    return jsonify({
        'message': 'Hello World'
    }), 400


@app.errorhandler(404)
def route_does_not_exist(error):
    return jsonify({
        'message': 'fucking route doesn\'t exit'
    })



app.register_blueprint(users_blueprint)


if __name__ == '__main__':
    app.run(debug=False, port=8000, host='0.0.0.0')