from flask import Flask, jsonify, make_response

app = Flask(__name__)

# Mozilla provides good references for Access Control at:
# https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Server-Side_Access_Control

def get_customers():
    return [
        {"id": 1, "name": "John Smith", "balance": "$2000"},
        {"id": 2, "name": "Ronald Alberts", "balance": "$500"},
        {"id": 3, "name": "Raymond Sparks", "balance": "$250"},
        {"id": 4, "name": "Amy Salvador", "balance": "$890"}
    ]


@app.route('/customers_api/customers', methods=['GET'])
def customers():
    """Return a JSON response for all customers."""
    sample_response = {
        "customers": get_customers()
    }
    # JSONify response
    response = make_response(jsonify(sample_response))

    # Add Access-Control-Allow-Origin header to allow cross-site request
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'

    return response