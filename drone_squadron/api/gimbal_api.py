from drone_squadron.api.base_api import BaseApi
from drone_squadron.crud.gimbal_crud import GimbalCrud


class GimbalApi(BaseApi):
    def __init__(self):
        super().__init__(GimbalCrud)
