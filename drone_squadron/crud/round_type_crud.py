from drone_squadron.crud.item_crud import ItemCrud
from drone_squadron.schema import round_type


class RoundType(ItemCrud):
    def __init__(self, connection=None):
        super().__init__(round_type, 'round_type', connection)


if __name__ == '__main__':
    with RoundType() as crud:
        result = crud.insert(
            scrap=25,
            name='SevenSixTwo',
            speed=45,
            radius=1,
            damage=5
        )
        last_id = result.inserted_primary_key[0]

    with RoundType() as crud:
        result = crud.select()
        rows = result.fetchall()
        print(rows)

    with RoundType() as crud:
        result = crud.update(item_id=last_id, name="Test")
        updated_params = result.last_updated_params()
        print(updated_params)

    with RoundType() as crud:
        result = crud.delete(item_id=last_id)
