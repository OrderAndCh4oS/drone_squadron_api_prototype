import pytest

from drone_squadron.app import create_app
from drone_squadron.load_fixtures import LoadFixtures


@pytest.fixture(scope="session")
def setup():
    from drone_squadron.database.engine import engine
    from drone_squadron.schema import metadata
    metadata.create_all(engine)
    yield
    metadata.drop_all(engine)


@pytest.fixture(scope='session')
def test_client():
    flask_app = create_app('test_flask.cfg')

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    test_client = flask_app.test_client()

    # Establish an application context before running the tests.
    context = flask_app.app_context()
    context.push()

    test_client.post(
        '/register',
        json={"username": "Sarcoma", "password": "password"},
        content_type="application/json"
    )

    test_client.get('/logout')

    LoadFixtures().load()

    yield test_client  # this is where the testing happens!

    context.pop()


@pytest.fixture()
def log_in(setup, test_client):
    response = test_client.post(
        '/login',
        json={"username": "Sarcoma", "password": "password"},
        content_type="application/json"
    )
    assert response.status_code == 200


@pytest.fixture()
def log_out(setup, test_client):
    response = test_client.get('/logout')
    assert response.status_code == 200
