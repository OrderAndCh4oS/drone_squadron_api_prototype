from sqlalchemy.engine import ResultProxy

from drone_squadron.crud.user_crud import UserCrud
from drone_squadron.schema import user


class TestUserCrud:
    crud = UserCrud

    def test_insert(self, connection):
        crud = self.crud(connection)
        result = crud.insert(username="Dave", password="secret")  # type: ResultProxy
        assert 1 == result.inserted_primary_key[0]

    def test_select(self, connection):
        crud = self.crud(connection)
        result = crud.select()  # type: ResultProxy
        rows = result.fetchall()
        assert "Dave" == rows[0][user.c.username]
        assert "secret" == rows[0][user.c.password]

    def test_update(self, connection):
        crud = self.crud(connection)
        result = crud.update(item_id=1, username="Dave_two", password="secret_two")  # type: ResultProxy
        assert {'id_1': 1, "username": "Dave_two", "password": "secret_two"} == result.last_updated_params()

    def test_delete(self, connection):
        crud = self.crud(connection)
        result = crud.delete(item_id=1)  # type: ResultProxy
        assert 1 == result.rowcount
