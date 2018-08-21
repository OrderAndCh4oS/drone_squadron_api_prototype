from drone_squadron.api.base_api import BaseApi
from drone_squadron.crud.scanner_crud import ScannerCrud


class ScannerApi(BaseApi):
    def __init__(self):
        super().__init__(ScannerCrud)
