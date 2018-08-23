class TestWeapon:

    def test_get(self, log_in, test_client):
        response = test_client.get('/weapon')
        data = response.get_json()[0]
        assert response.status_code == 200
        assert 1 == data['id']
        assert 'Shotgun' == data['name']
