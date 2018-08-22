import functools
from html import escape

from flask import request, session, g

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
from drone_squadron.crud.user_crud import UserCrud
from drone_squadron.authentication.login import Authentication
from drone_squadron.request.request_handler import RequestHandler
from drone_squadron.response.json_response import json_response


@app.before_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        with UserCrud() as crud:
            g.user = crud.select_by_id(user_id).fetchone()


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return json_response({'error': 'Not logged in'}, 401)

        return view(**kwargs)

    return wrapped_view


@app.route('/')
@login_required
def index():
    return json_response({'data': '%s is logged in' % escape(g.user['username'])})


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        user = Authentication.login(data['username'], data['password'])
        if user:
            session['user_id'] = user['id']
            return json_response({'data': '%d is logged in' % session['user_id']})
        else:
            return json_response({'error': 'Invalid credentials'}, 401)


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    g.user = None
    return json_response({'data': 'Logged out'})


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
