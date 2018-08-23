class TestSquadron:

    def test_post(self, log_in, test_client):
        response = test_client.post(
            '/squadron',
            json={"name": "Squad One"},
            content_type="application/json"
        )
        data = response.get_json()
        assert response.status_code == 200
        assert {'id': 1, 'name': 'Squad One', 'scrap': 1000} == data

    def test_post_unauthorized(self, log_out, test_client):
        response = test_client.post(
            '/squadron',
            json={"name": "Squad One"},
            content_type="application/json"
        )
        assert response.status_code == 401

    def test_get(self, log_in, test_client):
        response = test_client.get('/squadron/1')
        data = response.get_json()
        assert response.status_code == 200
        assert 1 == data['id']
        assert 'Squad One' == data['name']
        assert 1000 == data['scrap']
        assert 'created_at' in data
        assert 'updated_at' in data

    def test_put(self, log_in, test_client):
        response = test_client.put(
            '/squadron/1',
            json={"name": "Squad Two", "scrap": 900},
            content_type="application/json"
        )
        data = response.get_json()
        assert response.status_code == 200
        assert {'id_1': '1', 'name': 'Squad Two', 'scrap': 900} == data

    def test_delete(self, log_in, test_client):
        response = test_client.delete('/squadron/1')
        data = response.get_json()
        assert response.status_code == 200
        assert 1 == data['deleted_rows']
