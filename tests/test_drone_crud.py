from sqlalchemy.engine import ResultProxy

from drone_squadron.crud.drone_crud import DroneCrud
from drone_squadron.schema import steering, drone


class TestDroneCrud:
    crud = DroneCrud

    def test_insert(self, connection):
        crud = self.crud(connection)
        result = crud.insert(
            name="Drone One",
            weapon=1,
            gimbal=1,
            thruster=1,
            steering=1,
            scanner=1,
            squadron=1,
            status=0
        )  # type: ResultProxy
        assert 1 == result.inserted_primary_key[0]

    def test_select(self, connection):
        crud = self.crud(connection)
        result = crud.select()  # type: ResultProxy
        rows = result.fetchall()
        assert "Drone One" == rows[0][drone.c.name]

    def test_update(self, connection):
        crud = self.crud(connection)
        result = crud.update(item_id=1, name="Drone Two")  # type: ResultProxy
        assert {'id_1': 1, "name": "Drone Two"} == result.last_updated_params()

    def test_delete(self, connection):
        crud = self.crud(connection)
        result = crud.delete(item_id=1)  # type: ResultProxy
        assert 1 == result.rowcount
