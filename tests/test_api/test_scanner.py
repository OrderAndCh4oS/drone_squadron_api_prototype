class TestScanner:

    def test_get(self, log_in, test_client):
        response = test_client.get('/scanner')
        data = response.get_json()[0]
        assert response.status_code == 200
        assert 1 == data['id']
        assert 'SC200' == data['name']
        assert 200 == data['radius']
