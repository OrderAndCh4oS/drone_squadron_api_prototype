from drone_squadron.crud.round_type_crud import RoundTypeCrud
from drone_squadron.enums.round_type import RoundType

round_type_fixtures = (RoundTypeCrud, [
    {
        "name": "Shot",
        "type": RoundType.shot,
        "radius": 2,
        "damage": 54,
        "speed": 60,
        "colour": "orange",
        "scrap": 0
    },
    {
        "name": "SevenSixTwo",
        "type": RoundType.seven_six_two,
        "radius": 0.5,
        "damage": 3,
        "speed": 38,
        "colour": "red",
        "scrap": 0
    },
    {
        "name": "NineMM",
        "type": RoundType.nine_mm,
        "radius": 1,
        "damage": 8,
        "speed": 45,
        "colour": "green",
        "scrap": 0
    }
])
