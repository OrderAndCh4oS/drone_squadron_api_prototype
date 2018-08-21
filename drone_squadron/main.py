from html import escape

from flask import request, session

from drone_squadron.api.drone_api import DroneApi
from drone_squadron.api.squadron_api import SquadronApi
from drone_squadron.api.user_api import UserApi
from drone_squadron.app import app
from drone_squadron.request.request_handler import RequestHandler
from drone_squadron.response.json_response import json_response


@app.route('/')
def index():
    if 'username' in session:
        return json_response({'data': '%s is logged in' % escape(session['username'])})
    return json_response({'error': 'Not logged in'})


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        if 'username' in session:
            return json_response({'data': '%s is logged in' % escape(session['username'])})
        session['username'] = data['username']
        return json_response({'data': 'successfully logged in'})


@app.route('/logout')
def logout():
    session.pop('username', None)
    return json_response({'data': 'success'})


@app.route('/user', methods=['GET', 'POST'])
def user_list():
    return RequestHandler.list(UserApi())


@app.route('/user/<item_id>', methods=['GET', 'PUT', 'DELETE'])
def user_detail(item_id):
    return RequestHandler.detail(UserApi(), item_id)


@app.route('/squadron', methods=['GET', 'POST'])
def squadron_list():
    return RequestHandler.list(SquadronApi())


@app.route('/squadron/<item_id>', methods=['GET', 'PUT', 'DELETE'])
def squadron_detail(item_id):
    return RequestHandler.detail(SquadronApi(), item_id)


@app.route('/drone', methods=['GET', 'POST'])
def drone_list():
    return RequestHandler.list(DroneApi())


@app.route('/drone/<item_id>', methods=['GET', 'PUT', 'DELETE'])
def drone_detail(item_id):
    return RequestHandler.detail(DroneApi(), item_id)
