from sqlalchemy.engine import ResultProxy

from drone_squadron.crud.gimbal_crud import GimbalCrud
from drone_squadron.schema import gimbal


class TestGimbalCrud:
    crud = GimbalCrud

    def test_insert(self, setup):
        with self.crud() as crud:
            result = crud.insert(name="G60", angle=60, turning_speed=0.1)  # type: ResultProxy
            assert 1 == result.inserted_primary_key[0]

    def test_select(self, setup):
        with self.crud() as crud:
            result = crud.select()  # type: ResultProxy
            rows = result.fetchall()
            assert "G60" == rows[0][gimbal.c.name]
            assert 0.1 == rows[0][gimbal.c.turning_speed]

    def test_update(self, setup):
        with self.crud() as crud:
            result = crud.update(item_id=1, name="G80", angle=80, turning_speed=0.2)  # type: ResultProxy
            assert {'id_1': 1, "name": "G80", "angle": 80, "turning_speed": 0.2} == result.last_updated_params()

    def test_delete(self, setup):
        with self.crud() as crud:
            result = crud.delete(item_id=1)  # type: ResultProxy
            assert 1 == result.rowcount
