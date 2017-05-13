from flask import jsonify
from nxcontact.app import APP


@APP.route('/hello')
def hello_world():
    return jsonify({'message': 'Hello, World!'})


@APP.route('/echo/<message>')
def echo(message):
    return jsonify({'message': 'ECHO => {}'.format(message)})
