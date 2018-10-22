from sqlalchemy.engine import ResultProxy

from drone_squadron.api.base_api import BaseApi
from drone_squadron.crud.user_crud import UserCrud


class UserApi(BaseApi):
    def __init__(self):
        super().__init__(UserCrud)

    def post(self, data):
        with self.crud() as crud:
            result = crud.insert(**data)  # type: ResultProxy
            data = result.last_inserted_params()
            data.pop('password')
            data['id'] = result.inserted_primary_key[0]
        return data
