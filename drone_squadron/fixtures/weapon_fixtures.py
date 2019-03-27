from drone_squadron.crud.weapon_crud import WeaponCrud

weapon_fixtures = (WeaponCrud, [
    {"name": "Uzi", "fire_rate": 2, "round_type": 1, "scrap": 100},
    {"name": "Shotgun", "fire_rate": 7, "round_type": 2, "scrap": 200},
    {"name": "Rifle", "fire_rate": 10, "round_type": 3, "scrap": 300},
])
