from drone_squadron.crud.item_crud import ItemCrud
from drone_squadron.schema import gimbal


class GimbalCrud(ItemCrud):
    def __init__(self, connection=None):
        super().__init__(gimbal, 'gimbal', connection)


if __name__ == '__main__':
    with GimbalCrud() as crud:
        result = crud.insert(
            scrap=20,
            name='G120',
            angle=120,
            turning_speed=0.2
        )
        last_id = result.inserted_primary_key[0]

    with GimbalCrud() as crud:
        result = crud.select()
        rows = result.fetchall()
        print(rows)

    with GimbalCrud() as crud:
        result = crud.update(item_id=last_id, name="Test")
        updated_params = result.last_updated_params()
        print(updated_params)

    with GimbalCrud() as crud:
        result = crud.delete(item_id=last_id)
