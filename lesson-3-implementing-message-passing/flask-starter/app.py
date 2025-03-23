import json
from flask import Flask, jsonify, request, Response, make_response

from .services import retrieve_orders, create_order

app = Flask(__name__)


@app.route('/orders', methods=['GET', 'POST'])
def orders():
    if request.method == 'GET':
        return Response(json.dumps(retrieve_orders()), 200, {'Content-Type': 'application/json'})
    elif request.method == 'POST':
        request_body = request.json

        # JSONify response
        response = make_response(jsonify(create_order(request_body)), 201)

        # alternatively, but without status code:
        # response = jsonify(create_order(request_body))

        # Add Access-Control-Allow-Origin header to allow cross-site request
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'

        return response
    else:
        raise Exception('Unsupported HTTP request type.')
    

if __name__ == '__main__':
    app.run()
