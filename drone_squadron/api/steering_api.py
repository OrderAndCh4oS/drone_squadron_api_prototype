from drone_squadron.api.base_api import BaseApi
from drone_squadron.crud.steering_crud import SteeringCrud


class SteeringApi(BaseApi):
    def __init__(self):
        super().__init__(SteeringCrud)
