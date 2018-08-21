from drone_squadron.crud.base_crud import BaseCrud
from drone_squadron.schema import drone


class DroneCrud(BaseCrud):
    def __init__(self, connection=None):
        super().__init__(drone, connection)


if __name__ == '__main__':
    with DroneCrud() as crud:
        result = crud.insert(
            name='Drone One',
        )
        last_id = result.inserted_primary_key[0]

    with DroneCrud() as crud:
        result = crud.select()
        rows = result.fetchall()
        print("Select:", rows)

    with DroneCrud() as crud:
        result = crud.update(item_id=last_id, name="Test")
        updated_params = result.last_updated_params()
        print("Update:", updated_params)

    with DroneCrud() as crud:
        result = crud.delete(item_id=last_id)
