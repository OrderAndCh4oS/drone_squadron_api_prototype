from sqlalchemy.engine import ResultProxy

from drone_squadron.crud.thruster_crud import ThrusterCrud
from drone_squadron.schema import thruster


class TestThrusterCrud:
    crud = ThrusterCrud

    def test_insert(self, connection):
        crud = self.crud(connection)
        result = crud.insert(name="T10", thrust_power=10)  # type: ResultProxy
        assert 1 == result.inserted_primary_key[0]

    def test_select(self, connection):
        crud = self.crud(connection)
        result = crud.select()  # type: ResultProxy
        rows = result.fetchall()
        assert "T10" == rows[0][thruster.c.name]
        assert 10 == rows[0][thruster.c.thrust_power]

    def test_update(self, connection):
        crud = self.crud(connection)
        result = crud.update(item_id=1, name="T20", thrust_power=20)  # type: ResultProxy
        assert {'id_1': 1, "name": "T20", "thrust_power": 20} == result.last_updated_params()

    def test_delete(self, connection):
        crud = self.crud(connection)
        result = crud.delete(item_id=1)  # type: ResultProxy
        assert 1 == result.rowcount
