from sqlalchemy.engine import ResultProxy

from drone_squadron.crud.user_crud import UserCrud
from drone_squadron.schema import user


class TestUserCrud:
    crud = UserCrud

    def test_insert(self, setup):
        with self.crud() as crud:
            result = crud.insert(username="Dave", password="secret")  # type: ResultProxy
            assert 1 == result.inserted_primary_key[0]

    def test_select(self, setup):
        with self.crud() as crud:
            result = crud.select()  # type: ResultProxy
            rows = result.fetchall()
            assert "Dave" == rows[0][user.c.username]
            assert "pbkdf2:sha256:" == rows[0][user.c.password][:14]

    def test_update(self, setup):
        with self.crud() as crud:
            result = crud.update(item_id=1, username="Dave_two", password="secret_two")  # type: ResultProxy
            params = result.last_updated_params()
            assert "Dave_two" == params["username"]
            assert "pbkdf2:sha256:" == params["password"][:14]

    def test_delete(self, setup):
        with self.crud() as crud:
            result = crud.delete(item_id=1)  # type: ResultProxy
            assert 1 == result.rowcount
