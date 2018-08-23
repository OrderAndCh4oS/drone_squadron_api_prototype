class TestGimbal:

    def test_get(self, log_in, test_client):
        response = test_client.get('/gimbal')
        data = response.get_json()[0]
        assert response.status_code == 200
        assert 1 == data['id']
        assert 'Fixed' == data['name']
        assert 0 == data['angle']
        assert 0 == data['turning_speed']
