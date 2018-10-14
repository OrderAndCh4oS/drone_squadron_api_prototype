from sqlalchemy.engine import ResultProxy

from drone_squadron.crud.drone_crud import DroneCrud
from drone_squadron.schema import drone


class TestDroneCrud:
    crud = DroneCrud

    def test_insert(self, setup):
        with self.crud() as crud:
            result = crud.insert(
                name="Drone One",
                weapon=1,
                gimbal=1,
                thruster=1,
                steering=1,
                scanner=1,
                squadron=1,
            )  # type: ResultProxy
            assert 1 == result.inserted_primary_key[0]

    def test_select(self, setup):
        with self.crud() as crud:
            result = crud.select()  # type: ResultProxy
            rows = result.fetchall()
            assert "Drone One" == rows[0][drone.c.name]

    def test_update(self, setup):
        with self.crud() as crud:
            result = crud.update(item_id=1, name="Drone Two")  # type: ResultProxy
            assert {'id_1': 1, "name": "Drone Two"} == result.last_updated_params()

    def test_delete(self, setup):
        with self.crud() as crud:
            result = crud.delete(item_id=1)  # type: ResultProxy
            assert 1 == result.rowcount
