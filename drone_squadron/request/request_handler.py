from flask import request

from drone_squadron.response.json_response import json_response


class RequestHandler:
    @staticmethod
    def list(api):
        if request.method == 'POST':
            return json_response(api.post(request.get_json()))
        elif request.method == 'GET':
            return json_response(api.get())

    @staticmethod
    def detail(api, id):
        if request.method == 'PUT':
            return json_response(api.put(id, request.get_json()))
        elif request.method == 'DELETE':
            return json_response(api.delete(id))
        elif request.method == 'GET':
            return json_response(api.get_by_id(id))
