from drone_squadron.crud.round_type_crud import RoundTypeCrud
from drone_squadron.enums.round_type import RoundType

round_type_fixtures = (RoundTypeCrud, [
    {
        "name": "NineMM",
        "type": RoundType.nine_mm,
        "radius": 2,
        "damage": 6,
        "speed": 46,
        "colour": "green",
        "scrap": 0
    },
    {
        "name": "Shot",
        "type": RoundType.shot,
        "radius": 1,
        "damage": 2,
        "speed": 42,
        "colour": "orange",
        "scrap": 0
    },
    {
        "name": "SevenSixTwo",
        "type": RoundType.seven_six_two,
        "radius": 3,
        "damage": 18,
        "speed": 60,
        "colour": "red",
        "scrap": 0
    },
    {
        "name": "FourFive",
        "type": RoundType.four_five,
        "radius": 2,
        "damage": 11,
        "speed": 55,
        "colour": "blue",
        "scrap": 0
    }
])
