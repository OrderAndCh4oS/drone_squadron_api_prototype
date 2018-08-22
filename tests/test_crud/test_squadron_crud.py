from sqlalchemy.engine import ResultProxy

from drone_squadron.crud.squadron_crud import SquadronCrud
from drone_squadron.schema import squadron


class TestSquadronCrud:
    crud = SquadronCrud

    def test_insert(self, setup):
        with self.crud() as crud:
            result = crud.insert(name="Squad One", user=1)  # type: ResultProxy
            assert 1 == result.inserted_primary_key[0]

    def test_select(self, setup):
        with self.crud() as crud:
            result = crud.select()  # type: ResultProxy
            rows = result.fetchall()
            assert "Squad One" == rows[0][squadron.c.name]

    def test_update(self, setup):
        with self.crud() as crud:
            result = crud.update(item_id=1, name="Squad Two")  # type: ResultProxy
            assert {'id_1': 1, "name": "Squad Two"} == result.last_updated_params()

    def test_delete(self, setup):
        with self.crud() as crud:
            result = crud.delete(item_id=1)  # type: ResultProxy
            assert 1 == result.rowcount
