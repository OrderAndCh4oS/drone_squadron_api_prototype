class TestThruster:

    def test_get(self, log_in, test_client):
        response = test_client.get('/thruster')
        data = response.get_json()[0]
        assert response.status_code == 200
        assert 1 == data['id']
        assert 'T10' == data['name']
        assert 10 == data['thrust_power']
