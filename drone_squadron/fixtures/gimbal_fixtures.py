from drone_squadron.crud.gimbal_crud import GimbalCrud

gimbal_fixtures = (GimbalCrud, [
    {"name": "Fixed", "angle": 0, "turning_speed": 0, "scrap": 0},
    {"name": "G20", "angle": 20, "turning_speed": 0.1, "scrap": 40},
    {"name": "G40", "angle": 40, "turning_speed": 0.12, "scrap": 80},
    {"name": "G60", "angle": 60, "turning_speed": 0.14, "scrap": 120},
    {"name": "G90", "angle": 90, "turning_speed": 0.14, "scrap": 180},
    {"name": "G120", "angle": 120, "turning_speed": 0.16, "scrap": 240},
    {"name": "G180", "angle": 180, "turning_speed": 0.2, "scrap": 360},
    {"name": "G360", "angle": 360, "turning_speed": 0.25, "scrap": 620},
])
