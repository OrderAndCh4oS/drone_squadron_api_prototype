class TestDrone:

    def test_post(self, log_in, test_client):
        response = test_client.post(
            '/drone',
            json={"name": "Drone One", "squadron": 1},
            content_type="application/json"
        )
        data = response.get_json()
        assert response.status_code == 200
        assert 'id' in data
        assert 'name' in data
        assert 'kills' in data
        assert 'missions' in data
        assert 'value' in data
        assert 'weapon_name' in data
        assert 'gimbal_name' in data
        assert 'thruster_name' in data
        assert 'steering_name' in data
        assert 'scanner_name' in data

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
        assert 'id' in data
        assert 'name' in data
        assert 'kills' in data
        assert 'missions' in data
        assert 'value' in data
        assert 'weapon_name' in data
        assert 'gimbal_name' in data
        assert 'thruster_name' in data
        assert 'steering_name' in data
        assert 'scanner_name' in data


    def test_get_by_squadron(self, log_in, test_client):
        response = test_client.get('/squadron/1/drone')
        data = response.get_json()[0]
        assert response.status_code == 200
        assert 1 == data['id']
        assert 'id' in data
        assert 'name' in data
        assert 'kills' in data
        assert 'missions' in data
        assert 'value' in data
        assert 'weapon_name' in data
        assert 'gimbal_name' in data
        assert 'thruster_name' in data
        assert 'steering_name' in data
        assert 'scanner_name' in data


    def test_put(self, log_in, test_client):
        response = test_client.put(
            '/drone/1',
            json={"name": "Drone Two", "squadron": 1},
            content_type="application/json"
        )
        data = response.get_json()
        assert response.status_code == 200
        assert {'id_1': '1', 'name': 'Drone Two', "squadron": 1} == data

    def test_delete(self, log_in, test_client):
        response = test_client.delete('/drone/1')
        data = response.get_json()
        assert response.status_code == 200
        assert 1 == data['deleted_rows']
