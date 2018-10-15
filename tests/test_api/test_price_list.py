class TestPriceList:

    def test_get(self, log_in, test_client):
        response = test_client.get('/price-list')
        data = response.get_json()[0]
        assert response.status_code == 200
        assert 'weapon' == data['item']
