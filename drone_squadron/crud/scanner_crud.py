from drone_squadron.crud.item_crud import ItemCrud
from drone_squadron.schema import scanner


class ScannerCrud(ItemCrud):
    def __init__(self, connection=None):
        super().__init__(scanner, 'scanner', connection)


if __name__ == '__main__':
    with ScannerCrud() as crud:
        result = crud.insert(
            scrap=20,
            name='SC120',
            radius=120,
        )
        last_id = result.inserted_primary_key[0]

    with ScannerCrud() as crud:
        result = crud.select()
        rows = result.fetchall()
        print(rows)

    with ScannerCrud() as crud:
        result = crud.update(item_id=last_id, name="Test")
        updated_params = result.last_updated_params()
        print(updated_params)

    with ScannerCrud() as crud:
        result = crud.delete(item_id=last_id)
