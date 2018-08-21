from html import escape

from flask import request, session

from drone_squadron.api.drone_api import DroneApi
from drone_squadron.api.gimbal_api import GimbalApi
from drone_squadron.api.round_type_api import RoundTypeApi
from drone_squadron.api.scanner_api import ScannerApi
from drone_squadron.api.squadron_api import SquadronApi
from drone_squadron.api.steering_api import SteeringApi
from drone_squadron.api.thruster_api import ThrusterApi
from drone_squadron.api.user_api import UserApi
from drone_squadron.api.weapon_api import WeaponApi
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


@app.route('/weapon', methods=['GET'])
def weapon_list():
    return json_response(WeaponApi().get())


@app.route('/round-type', methods=['GET'])
def round_type_list():
    return json_response(RoundTypeApi().get())


@app.route('/scanner', methods=['GET'])
def scanner_list():
    return json_response(ScannerApi().get())


@app.route('/steering', methods=['GET'])
def steering_list():
    return json_response(SteeringApi().get())


@app.route('/thruster', methods=['GET'])
def thruster_list():
    return json_response(ThrusterApi().get())


@app.route('/gimbal', methods=['GET'])
def gimbal_list():
    return json_response(GimbalApi().get())
