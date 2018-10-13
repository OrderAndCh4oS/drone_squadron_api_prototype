from sqlalchemy.engine import ResultProxy

from drone_squadron.api.base_api import BaseApi
from drone_squadron.crud.drone_crud import DroneCrud


class DroneApi(BaseApi):
    def __init__(self):
        super().__init__(DroneCrud)

    def get_by_squadron_id(self, squadron_id):
        with self.table() as crud:
            result = crud.select_by_squadron_id(squadron_id)  # type: ResultProxy
            data = result.fetchall()
        return data
