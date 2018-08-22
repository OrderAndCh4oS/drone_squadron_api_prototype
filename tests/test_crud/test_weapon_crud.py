from sqlalchemy.engine import ResultProxy

from drone_squadron.crud.weapon_crud import WeaponCrud
from drone_squadron.schema import weapon


class TestWeaponCrud:
    crud = WeaponCrud

    def test_insert(self, setup):
        with self.crud() as crud:
            result = crud.insert(name="Rifle", fire_rate=5)  # type: ResultProxy
            assert 1 == result.inserted_primary_key[0]

    def test_select(self, setup):
        with self.crud() as crud:
            result = crud.select()  # type: ResultProxy
            rows = result.fetchall()
            assert "Rifle" == rows[0][weapon.c.name]
            assert 5 == rows[0][weapon.c.fire_rate]

    def test_update(self, setup):
        with self.crud() as crud:
            result = crud.update(item_id=1, name="AWP", fire_rate=10)  # type: ResultProxy
            assert {'id_1': 1, "name": "AWP", "fire_rate": 10} == result.last_updated_params()

    def test_delete(self, setup):
        with self.crud() as crud:
            result = crud.delete(item_id=1)  # type: ResultProxy
            assert 1 == result.rowcount
