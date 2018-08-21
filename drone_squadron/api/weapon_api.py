from drone_squadron.api.base_api import BaseApi
from drone_squadron.crud.weapon_crud import WeaponCrud


class WeaponApi(BaseApi):
    def __init__(self):
        super().__init__(WeaponCrud)
