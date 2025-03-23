import json
from flask import Flask, jsonify, request, Response

from .services import retrieve_orders, create_order

app = Flask(__name__)


@app.route('/orders', methods=['GET', 'POST'])
def orders():
    if request.method == 'GET':
        return Response(json.dumps(retrieve_orders()), 200, {'Content-Type': 'application/json'})
    elif request.method == 'POST':
        order = request.json
        return jsonify(create_order(order))
    else:
        raise Exception('Unsupported HTTP request type.')
    

if __name__ == '__main__':
    app.run()
