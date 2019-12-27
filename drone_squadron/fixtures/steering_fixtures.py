from drone_squadron.crud.steering_crud import SteeringCrud

steering_fixtures = (SteeringCrud, [
    {"name": "S4", "turning_speed": 0.4, "scrap": 0},
    {"name": "S6", "turning_speed": 0.6, "scrap": 40},
    {"name": "S8", "turning_speed": 0.8, "scrap": 60},
    {"name": "S10", "turning_speed": 1.0, "scrap": 100},
    {"name": "S12", "turning_speed": 1.2, "scrap": 160},
    {"name": "S15", "turning_speed": 1.5, "scrap": 320},
    {"name": "S20", "turning_speed": 2, "scrap": 500},
])
