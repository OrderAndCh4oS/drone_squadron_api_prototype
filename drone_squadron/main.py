from flask_cors import CORS

from drone_squadron.app import create_app

app = create_app('flask.cfg')
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}}, supports_credentials=True)
