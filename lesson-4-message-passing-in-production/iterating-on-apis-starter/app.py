import json
from flask import Flask, jsonify, request

from .services import retrieve_orders, create_order

app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify({'response': 'Hello World!'})


@app.route('/api/orders/computers', methods=['GET', 'POST'])
def computers():
    if request.method == 'GET':
        return jsonify(retrieve_orders())
    elif request.method == 'POST':
        request_body = request.json
        return jsonify(create_order(request_body))
    else:
        raise Exception('Unsupported HTTP request type.')

# or - to differentiate the version of the API:
# @app.route('/api/v2/orders/computers', methods=['GET', 'POST'], endpoint='orders_v2')
@app.route('/api/v2/orders/computers', methods=['GET', 'POST'])
def computers_v2():
    if request.method == 'GET':
        return jsonify(retrieve_orders())
    elif request.method == 'POST':
        request_body = request.json
        return jsonify(create_order(request_body))
    else:
        raise Exception('Unsupported HTTP request type.')


if __name__ == '__main__':
    app.run()
