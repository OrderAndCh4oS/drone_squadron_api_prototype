from drone_squadron.api.base_api import BaseApi
from drone_squadron.crud.round_type_crud import RoundTypeCrud


class RoundTypeApi(BaseApi):
    def __init__(self):
        super().__init__(RoundTypeCrud)
