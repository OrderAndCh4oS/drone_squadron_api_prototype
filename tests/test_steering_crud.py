from sqlalchemy.engine import ResultProxy

from drone_squadron.crud.steering_crud import SteeringCrud
from drone_squadron.schema import steering


class TestSteeringCrud:
    crud = SteeringCrud

    def test_insert(self, connection):
        crud = self.crud(connection)
        result = crud.insert(name="ST100", turning_speed=0.3)  # type: ResultProxy
        assert 1 == result.inserted_primary_key[0]

    def test_select(self, connection):
        crud = self.crud(connection)
        result = crud.select()  # type: ResultProxy
        rows = result.fetchall()
        assert "ST100" == rows[0][steering.c.name]
        assert 0.3 == rows[0][steering.c.turning_speed]

    def test_update(self, connection):
        crud = self.crud(connection)
        result = crud.update(item_id=1, name="ST200", turning_speed=0.5)  # type: ResultProxy
        assert {'id_1': 1, "name": "ST200", "turning_speed": 0.5} == result.last_updated_params()

    def test_delete(self, connection):
        crud = self.crud(connection)
        result = crud.delete(item_id=1)  # type: ResultProxy
        assert 1 == result.rowcount
