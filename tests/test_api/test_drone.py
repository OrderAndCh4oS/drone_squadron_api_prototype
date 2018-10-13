class TestDrone:

    def test_post(self, log_in, test_client):
        response = test_client.post(
            '/drone',
            json={"name": "Drone One", "squadron": 1},
            content_type="application/json"
        )
        data = response.get_json()
        assert response.status_code == 200
        assert {'id': 1, 'name': 'Drone One', 'kills': 0, 'missions': 0, 'status': 0, 'value': 0, 'squadron': 1} == data

    def test_post_unauthorized(self, log_out, test_client):
        response = test_client.post(
            '/drone',
            json={"name": "Drone One"},
            content_type="application/json"
        )
        assert response.status_code == 401

    def test_get(self, log_in, test_client):
        response = test_client.get('/drone/1')
        data = response.get_json()
        assert response.status_code == 200
        assert 1 == data['id']
        assert 'Drone One' == data['name']
        assert 'created_at' in data
        assert 'updated_at' in data

    def test_get_by_squadron(self, log_in, test_client):
        response = test_client.get('/squadron/1/drone')
        data = response.get_json()[0]
        assert response.status_code == 200
        assert 1 == data['id']
        assert 'Drone One' == data['name']
        assert 'created_at' in data
        assert 'updated_at' in data

    def test_put(self, log_in, test_client):
        response = test_client.put(
            '/drone/1',
            json={"name": "Drone Two"},
            content_type="application/json"
        )
        data = response.get_json()
        assert response.status_code == 200
        assert {'id_1': '1', 'name': 'Drone Two'} == data

    def test_delete(self, log_in, test_client):
        response = test_client.delete('/drone/1')
        data = response.get_json()
        assert response.status_code == 200
        assert 1 == data['deleted_rows']
