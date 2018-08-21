from drone_squadron.crud.item_crud import ItemCrud
from drone_squadron.schema import thruster


class ThrusterCrud(ItemCrud):
    def __init__(self, connection=None):
        super().__init__(thruster, 'thruster', connection)


if __name__ == '__main__':
    with ThrusterCrud() as crud:
        result = crud.insert(
            scrap=20,
            name='T10',
            power=10
        )
        last_id = result.inserted_primary_key[0]

    with ThrusterCrud() as crud:
        result = crud.select()
        rows = result.fetchall()
        print(rows)

    with ThrusterCrud() as crud:
        result = crud.update(item_id=last_id, name="Test")
        updated_params = result.last_updated_params()
        print(updated_params)

    with ThrusterCrud() as crud:
        result = crud.delete(item_id=last_id)
