from flask import request

from drone_squadron.response.json_response import json_response
from exception.exceptions import APIException


class JsonRequestHandler:
    @staticmethod
    def get(api):
        if request.method == 'GET':
            try:
                return json_response(api.get())
            except APIException as error:
                return json_response({'error': error}, 406)

    @staticmethod
    def post(api):
        if request.method == 'POST':
            try:
                return json_response(api.post(request.get_json()))
            except APIException as error:
                return json_response({'error': error}, 406)

    @staticmethod
    def put(api, item_id):
        if request.method == 'PUT':
            try:
                return json_response(api.put(item_id, request.get_json()))
            except APIException as error:
                return json_response({'error': error}, 406)

    @staticmethod
    def delete(api, item_id):
        if request.method == 'DELETE':
            try:
                return json_response(api.delete(item_id))
            except APIException as error:
                return json_response({'error': error}, 406)

    @staticmethod
    def list(api):
        if request.method == 'POST':
            try:
                return json_response(api.post(request.get_json()))
            except APIException as error:
                return json_response({'error': error}, 406)
        elif request.method == 'GET':
            try:
                return json_response(api.get())
            except APIException as error:
                return json_response({'error': error}, 406)

    @staticmethod
    def detail(api, item_id):
        if request.method == 'PUT':
            try:
                return json_response(api.put(item_id, request.get_json()))
            except APIException as error:
                return json_response({'error': error}, 406)
        elif request.method == 'DELETE':
            try:
                return json_response(api.delete(item_id))
            except APIException as error:
                return json_response({'error': error}, 406)
        elif request.method == 'GET':
            try:
                return json_response(api.get_by_id(item_id))
            except APIException as error:
                return json_response({'error': error}, 406)
