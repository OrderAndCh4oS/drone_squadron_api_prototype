from sqlalchemy.engine import ResultProxy

from drone_squadron.api.base_api import BaseApi
from drone_squadron.crud.squadron_crud import SquadronCrud
from drone_squadron.error.error import ValidationError
from drone_squadron.model.squadron_model import SquadronModel


class SquadronApi(BaseApi):
    def __init__(self):
        super().__init__(SquadronCrud)

    def post(self, data):
        data['scrap'] = 1000
        model = SquadronModel(data.get('name'), data.get('scrap'))
        if not model.validate():
            return ValidationError(model.get_errors())
        with self.crud() as crud:
            result = crud.insert(**data)  # type: ResultProxy
            data = result.last_inserted_params()
            data['id'] = result.inserted_primary_key[0]
        return data

    def spend_scrap(self, squadron_id, cost):
        with self.crud() as crud:
            crud.spend_scrap(squadron_id, cost)
