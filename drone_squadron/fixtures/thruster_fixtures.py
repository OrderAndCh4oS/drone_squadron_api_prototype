from drone_squadron.crud.thruster_crud import ThrusterCrud

thruster_fixtures = (ThrusterCrud, [
    {"name": "T10", "thrust_power": 10, "scrap": 0},
    {"name": "T12", "thrust_power": 12, "scrap": 20},
    {"name": "T15", "thrust_power": 15, "scrap": 40},
    {"name": "T18", "thrust_power": 18, "scrap": 80},
    {"name": "T20", "thrust_power": 20, "scrap": 200},
    {"name": "T25", "thrust_power": 25, "scrap": 300},
    {"name": "T40", "thrust_power": 40, "scrap": 600},
])
