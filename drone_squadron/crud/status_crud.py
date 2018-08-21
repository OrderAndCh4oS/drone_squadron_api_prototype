from drone_squadron.crud.base_crud import BaseCrud
from drone_squadron.enums import Status
from drone_squadron.schema import status


class StatusCrud(BaseCrud):
    def __init__(self, connection=None):
        super().__init__(status, connection)


if __name__ == '__main__':
    with StatusCrud() as crud:
        result = crud.insert(
            value=Status.ready,
        )
        last_id = result.inserted_primary_key[0]

    with StatusCrud() as crud:
        result = crud.select()
        rows = result.fetchall()
        print(rows)

    with StatusCrud() as crud:
        result = crud.update(item_id=last_id, value=Status.damaged)
        updated_params = result.last_updated_params()
        print(updated_params)

    with StatusCrud() as crud:
        result = crud.delete(item_id=last_id)
