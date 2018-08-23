class TestAuth:

    def test_unauthorized(self, setup, test_client):
        response = test_client.get('/')
        assert response.status_code == 401

    def test_login(self, setup, test_client):
        response = test_client.post(
            '/login',
            json={"username": "unknown", "password": "not_my_password"},
            content_type="application/json"
        )
        assert response.status_code == 401

    def test_register(self, setup, test_client):
        response = test_client.post(
            '/register',
            json={"username": "Sean", "password": "password"},
            content_type="application/json"
        )
        assert response.status_code == 200
        assert 'Sean' == response.get_json()['username']
        assert 'password' in response.get_json()

    def test_authorized(self, setup, test_client):
        response = test_client.get('/')
        assert response.status_code == 200
