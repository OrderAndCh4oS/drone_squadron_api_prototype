from drone_squadron.crud.status_crud import StatusCrud

status_fixtures = (StatusCrud, [
    {"value": "ready"},
    {"value": "damaged"},
    {"value": "repairing"},
    {"value": "destroyed"},
    {"value": "upgrading"},
])
