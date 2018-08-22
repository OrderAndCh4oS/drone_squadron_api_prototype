from werkzeug.security import check_password_hash

from drone_squadron.crud.user_crud import UserCrud
from drone_squadron.schema import user


class Authentication:

    @staticmethod
    def login(username, password):
        with UserCrud() as crud:
            found_user = crud.select_by_username(username).fetchone()
        if found_user is not None and check_password_hash(found_user[user.c.password], password):
            return found_user
        return None
