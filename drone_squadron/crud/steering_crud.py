from drone_squadron.crud.item_crud import ItemCrud
from drone_squadron.schema import steering


class SteeringCrud(ItemCrud):
    def __init__(self, connection=None):
        super().__init__(steering, 'steering', connection)


if __name__ == '__main__':
    with SteeringCrud() as crud:
        result = crud.insert(
            scrap=20,
            name='ST120',
            turning_speed=0.2
        )
        last_id = result.inserted_primary_key[0]

    with SteeringCrud() as crud:
        result = crud.select()
        rows = result.fetchall()
        print(rows)

    with SteeringCrud() as crud:
        result = crud.update(item_id=last_id, name="Test")
        updated_params = result.last_updated_params()
        print(updated_params)

    with SteeringCrud() as crud:
        result = crud.delete(item_id=last_id)
