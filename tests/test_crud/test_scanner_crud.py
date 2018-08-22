from sqlalchemy.engine import ResultProxy

from drone_squadron.crud.scanner_crud import ScannerCrud
from drone_squadron.schema import scanner


class TestScannerCrud:
    crud = ScannerCrud

    def test_insert(self, setup):
        with self.crud() as crud:
            result = crud.insert(name="SC100", radius=100)  # type: ResultProxy
            assert 1 == result.inserted_primary_key[0]

    def test_select(self, setup):
        with self.crud() as crud:
            result = crud.select()  # type: ResultProxy
            rows = result.fetchall()
            assert "SC100" == rows[0][scanner.c.name]
            assert 100 == rows[0][scanner.c.radius]

    def test_update(self, setup):
        with self.crud() as crud:
            result = crud.update(item_id=1, name="SC200", radius=200)  # type: ResultProxy
            assert {'id_1': 1, "name": "SC200", "radius": 200} == result.last_updated_params()

    def test_delete(self, setup):
        with self.crud() as crud:
            result = crud.delete(item_id=1)  # type: ResultProxy
            assert 1 == result.rowcount
