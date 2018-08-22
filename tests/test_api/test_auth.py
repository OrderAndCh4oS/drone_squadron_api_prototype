from flask.testing import FlaskClient


class TestAuth:

    def test_unauthorized(self, setup, test_client):
        response = test_client.get('/')
        assert response.status_code == 401

    def test_login(self, setup, test_client: FlaskClient):
        response = test_client.post(
            '/login',
            json={"username": "unknown", "password": "not_my_password"},
            content_type="application/json"
        )
        assert response.status_code == 401
