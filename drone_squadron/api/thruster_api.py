from drone_squadron.api.base_api import BaseApi
from drone_squadron.crud.thruster_crud import ThrusterCrud


class ThrusterApi(BaseApi):
    def __init__(self):
        super().__init__(ThrusterCrud)
