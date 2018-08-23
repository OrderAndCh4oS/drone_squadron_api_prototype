class TestRoundType:

    def test_get(self, log_in, test_client):
        response = test_client.get('/round-type')
        data = response.get_json()[0]
        assert response.status_code == 200
        assert 1 == data['id']
        assert 'Shot' == data['name']
