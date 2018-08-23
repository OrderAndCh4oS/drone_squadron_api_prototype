from drone_squadron.crud.thruster_crud import ThrusterCrud

thruster_fixtures = (ThrusterCrud, [
    {"name": "T10", "thrust_power": 10, "scrap": 0},
    {"name": "T12", "thrust_power": 12, "scrap": 120},
    {"name": "T15", "thrust_power": 15, "scrap": 225},
    {"name": "T18", "thrust_power": 18, "scrap": 360},
    {"name": "T20", "thrust_power": 20, "scrap": 400},
    {"name": "T25", "thrust_power": 25, "scrap": 500},
])
