from drone_squadron.crud.item_crud import ItemCrud
from drone_squadron.schema import weapon


class WeaponCrud(ItemCrud):
    def __init__(self, connection=None):
        super().__init__(weapon, 'weapon', connection)


if __name__ == '__main__':
    with WeaponCrud() as crud:
        result = crud.insert(
            scrap=20,
            name='T120',
            fire_rate=5,
            round_type=1
        )
        last_id = result.inserted_primary_key[0]

    with WeaponCrud() as crud:
        result = crud.select()
        rows = result.fetchall()
        print(rows)

    with WeaponCrud() as crud:
        result = crud.update(item_id=last_id, name="Test")
        updated_params = result.last_updated_params()
        print(updated_params)

    with WeaponCrud() as crud:
        result = crud.delete(item_id=last_id)
