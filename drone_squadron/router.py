import functools
from html import escape

from flask import request, session, g, Blueprint

from drone_squadron.api.drone_api import DroneApi
from drone_squadron.api.gimbal_api import GimbalApi
from drone_squadron.api.round_type_api import RoundTypeApi
from drone_squadron.api.scanner_api import ScannerApi
from drone_squadron.api.squadron_api import SquadronApi
from drone_squadron.api.steering_api import SteeringApi
from drone_squadron.api.thruster_api import ThrusterApi
from drone_squadron.api.user_api import UserApi
from drone_squadron.api.weapon_api import WeaponApi
from drone_squadron.authentication.login import Authentication
from drone_squadron.crud.user_crud import UserCrud
from drone_squadron.request.request_handler import JsonRequestHandler
from drone_squadron.response.json_response import json_response

router = Blueprint('router', __name__)


@router.before_request
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


def admin_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return json_response({'error': 'Not logged in'}, 401)
        if 'admin' not in g.roles:
            return json_response({'error': 'Not authorized'}, 401)

        return view(**kwargs)

    return wrapped_view


@router.route('/')
@login_required
def index():
    return json_response({'data': '%s is logged in' % escape(g.user['username'])})


@router.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        data = UserApi().post(request.get_json())
        session['user_id'] = data['id']

        return JsonRequestHandler.post(UserApi())


@router.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        user = Authentication.login(data['username'], data['password'])
        if user:
            session['user_id'] = user['id']
            return json_response({'data': '%d is logged in' % session['user_id']})
        else:
            return json_response({'error': 'Invalid credentials'}, 401)


@router.route('/logout')
def logout():
    session.pop('user_id', None)
    g.user = None
    return json_response({'data': 'Logged out'})


@router.route('/user', methods=['GET', 'POST'])
@login_required
def users():
    return JsonRequestHandler.get(UserApi())


@router.route('/user/<item_id>', methods=['GET', 'PUT', 'DELETE'])
@login_required
def user_detail(item_id):
    return JsonRequestHandler.detail(UserApi(), item_id)


@router.route('/squadron', methods=['GET', 'POST'])
@login_required
def squadron_list():
    return JsonRequestHandler.list(SquadronApi())


@router.route('/squadron/<item_id>', methods=['GET', 'PUT', 'DELETE'])
@login_required
def squadron_detail(item_id):
    return JsonRequestHandler.detail(SquadronApi(), item_id)


@router.route('/drone', methods=['GET', 'POST'])
@login_required
def drone_list():
    return JsonRequestHandler.list(DroneApi())


@router.route('/drone/<item_id>', methods=['GET', 'PUT', 'DELETE'])
@login_required
def drone_detail(item_id):
    return JsonRequestHandler.detail(DroneApi(), item_id)


@router.route('/weapon', methods=['GET'])
@login_required
def weapon_list():
    return json_response(WeaponApi().get())


@router.route('/round-type', methods=['GET'])
@login_required
def round_type_list():
    return json_response(RoundTypeApi().get())


@router.route('/scanner', methods=['GET'])
@login_required
def scanner_list():
    return json_response(ScannerApi().get())


@router.route('/steering', methods=['GET'])
@login_required
def steering_list():
    return json_response(SteeringApi().get())


@router.route('/thruster', methods=['GET'])
@login_required
def thruster_list():
    return json_response(ThrusterApi().get())


@router.route('/gimbal', methods=['GET'])
@login_required
def gimbal_list():
    return json_response(GimbalApi().get())
