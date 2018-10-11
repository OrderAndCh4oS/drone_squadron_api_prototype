from drone_squadron.api.base_api import BaseApi
from drone_squadron.crud.price_crud import PriceCrud


class PriceApi(BaseApi):
    def __init__(self):
        super().__init__(PriceCrud)
