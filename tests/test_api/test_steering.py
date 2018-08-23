class TestSteering:

    def test_get(self, log_in, test_client):
        response = test_client.get('/steering')
        data = response.get_json()[0]
        assert response.status_code == 200
        assert 1 == data['id']
        assert 'S4' == data['name']
        assert 0.4 == data['turning_speed']
