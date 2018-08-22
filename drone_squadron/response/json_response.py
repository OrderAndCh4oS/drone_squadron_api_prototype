import json

from drone_squadron.transformer.json_transformer import JsonTransformer


def json_response(data, status=200):
    data = JsonTransformer().get_data(data)
    from drone_squadron.main import app
    response = app.response_class(
        response=json.dumps(data),
        status=status,
        mimetype='application/json'
    )
    return response
