from sqlalchemy.engine import ResultProxy

from drone_squadron.crud.status_crud import StatusCrud
from drone_squadron.schema import status
from drone_squadron.enums import Status


class TestStatusCrud:
    crud = StatusCrud

    def test_insert(self, connection):
        crud = self.crud(connection)
        result = crud.insert(value=Status.ready)  # type: ResultProxy
        assert 1 == result.inserted_primary_key[0]

    def test_select(self, connection):
        crud = self.crud(connection)
        result = crud.select()  # type: ResultProxy
        rows = result.fetchall()
        assert Status.ready == rows[0][status.c.value]

    def test_update(self, connection):
        crud = self.crud(connection)
        result = crud.update(item_id=1, value=Status.damaged)  # type: ResultProxy
        assert {'id_1': 1, "value": Status.damaged} == result.last_updated_params()

    def test_delete(self, connection):
        crud = self.crud(connection)
        result = crud.delete(item_id=1)  # type: ResultProxy
        assert 1 == result.rowcount
