from drone_squadron.api.base_api import BaseApi
from drone_squadron.crud.squadron_crud import SquadronCrud


class SquadronApi(BaseApi):
    def __init__(self):
        super().__init__(SquadronCrud)
