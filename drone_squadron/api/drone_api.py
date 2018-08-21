from drone_squadron.api.base_api import BaseApi
from drone_squadron.crud.drone_crud import DroneCrud


class DroneApi(BaseApi):
    def __init__(self):
        super().__init__(DroneCrud)
