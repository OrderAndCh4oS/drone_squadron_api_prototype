from drone_squadron.crud.weapon_crud import WeaponCrud

weapon_fixtures = (WeaponCrud, [
    {"name": "Uzi", "fire_rate": 3, "round_type": 1, "scrap": 100},
    {"name": "Shotgun", "fire_rate": 8, "round_type": 2, "scrap": 200},
    {"name": "Rifle", "fire_rate": 6, "round_type": 3, "scrap": 300},
    {"name": "Vector", "fire_rate": 2.5, "round_type": 4, "scrap": 500},
    {"name": "Minigun", "fire_rate": 3.5, "round_type": 3, "scrap": 1000},
])
