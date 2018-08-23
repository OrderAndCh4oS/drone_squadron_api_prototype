class TestAuth:

    def test_unauthorized(self, setup, log_out, test_client):
        response = test_client.get('/')
        assert response.status_code == 401

    def test_login_failure(self, setup, log_out, test_client):
        response = test_client.post(
            '/login',
            json={"username": "unknown", "password": "not_my_password"},
            content_type="application/json"
        )
        assert response.status_code == 401

    def test_register(self, setup, log_out, test_client):
        response = test_client.post(
            '/register',
            json={"username": "Sean", "password": "password"},
            content_type="application/json"
        )
        data = response.get_json()
        assert response.status_code == 200
        assert 'Sean' == data['username']

    def test_authorized(self, setup, log_in, test_client):
        response = test_client.get('/')
        assert response.status_code == 200

    def test_logout(self, setup, log_in, test_client):
        response = test_client.get('/logout')
        assert response.status_code == 200
        response = test_client.get('/')
        assert response.status_code == 401

    def test_login_success(self, setup, log_out, test_client):
        response = test_client.post(
            '/login',
            json={"username": "Sean", "password": "password"},
            content_type="application/json"
        )
        assert response.status_code == 200
