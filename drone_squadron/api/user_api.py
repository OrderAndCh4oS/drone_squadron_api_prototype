from drone_squadron.api.base_api import BaseApi
from drone_squadron.crud.user_crud import UserCrud


class UserApi(BaseApi):
    def __init__(self):
        super().__init__(UserCrud)
