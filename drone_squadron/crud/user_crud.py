from werkzeug.security import generate_password_hash

from drone_squadron.crud.base_crud import BaseCrud
from drone_squadron.schema import user


class UserCrud(BaseCrud):
    def __init__(self, connection=None):
        super().__init__(user, connection)

    def insert(self, **kwargs):
        password = kwargs.pop('password')
        hashed_password = generate_password_hash(password)
        return self.connection.execute(
            self.table.insert(),
            password=hashed_password,
            **kwargs
        )

    def update(self, **kwargs):
        item_id = kwargs.pop('item_id')
        password = kwargs.pop('password')
        hashed_password = generate_password_hash(password)
        return self.connection.execute(
            self.table.update().where(self.table.c.id == item_id),
            password=hashed_password,
            **kwargs
        )

    def select_by_username(self, username):
        return self.execute(self.table.select().where(user.c.username == username))


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

    # with UserCrud() as crud:
    #     crud.delete(last_id)
