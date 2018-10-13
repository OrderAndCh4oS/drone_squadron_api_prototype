from drone_squadron.crud.steering_crud import SteeringCrud

steering_fixtures = (SteeringCrud, [
    {"value": "ready"},
    {"value": "damaged"},
    {"value": "repairing"},
    {"value": "destroyed"},
])
