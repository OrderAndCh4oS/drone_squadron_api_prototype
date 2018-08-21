from drone_squadron.crud.base_crud import BaseCrud
from drone_squadron.schema import user


class UserCrud(BaseCrud):
    def __init__(self, connection=None):
        super().__init__(user, connection)


if __name__ == '__main__':
    with UserCrud() as crud:
        result = crud.insert(username="Sean", password="secret")
        last_id = result.inserted_primary_key[0]

    with UserCrud() as crud:
        result = crud.select()
        rows = result.fetchall()

    print(rows)

    with UserCrud() as crud:
        result = crud.update(item_id=last_id, username="Sarcoma", password="too_secret")
        updated_data = result.last_updated_params()

    print(updated_data)

    with UserCrud() as crud:
        result = crud.select()
        rows = result.fetchall()

    print(rows)

    with UserCrud() as crud:
        crud.delete(last_id)
