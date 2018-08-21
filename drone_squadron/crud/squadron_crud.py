from drone_squadron.crud.base_crud import BaseCrud
from drone_squadron.schema import squadron


class SquadronCrud(BaseCrud):
    def __init__(self, connection=None):
        super().__init__(squadron, connection)


if __name__ == '__main__':
    with SquadronCrud() as crud:
        result = crud.insert(
            name='Squadron Name',
            user=1
        )
        last_id = result.inserted_primary_key[0]

    with SquadronCrud() as crud:
        result = crud.select()
        rows = result.fetchall()
        print(rows)

    with SquadronCrud() as crud:
        result = crud.update(item_id=last_id, name="Test")
        updated_params = result.last_updated_params()
        print(updated_params)

    with SquadronCrud() as crud:
        result = crud.delete(item_id=last_id)
