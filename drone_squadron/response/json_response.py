import json

from drone_squadron.app import app
from drone_squadron.transformer.json_transformer import JsonTransformer


def json_response(data):
    data = JsonTransformer().get_data(data)
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response
