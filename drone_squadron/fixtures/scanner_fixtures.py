from drone_squadron.crud.scanner_crud import ScannerCrud

scanner_fixtures = (ScannerCrud, [
    {"name": "SC300", "radius": 300, "scrap": 0},
    {"name": "SC400", "radius": 400, "scrap": 200},
    {"name": "SC500", "radius": 500, "scrap": 300},
    {"name": "SC600", "radius": 600, "scrap": 400},
    {"name": "SC700", "radius": 700, "scrap": 500},
    {"name": "SC800", "radius": 800, "scrap": 800},
    {"name": "SC900", "radius": 900, "scrap": 1000},
])
