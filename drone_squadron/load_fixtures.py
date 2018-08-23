from drone_squadron.database.database import Database
from drone_squadron.fixtures.gimbal_fixtures import gimbal_fixtures
from drone_squadron.fixtures.round_type_fixtures import round_type_fixtures
from drone_squadron.fixtures.scanner_fixtures import scanner_fixtures
from drone_squadron.fixtures.steering_fixtures import steering_fixtures
from drone_squadron.fixtures.thruster_fixtures import thruster_fixtures
from drone_squadron.fixtures.weapon_fixtures import weapon_fixtures
from drone_squadron.schema import metadata


class LoadFixtures:
    def __init__(self):
        self.fixtures = [
            round_type_fixtures,
            weapon_fixtures,
            scanner_fixtures,
            thruster_fixtures,
            steering_fixtures,
            gimbal_fixtures
        ]

    def load(self):
        for fixture in self.fixtures:
            for row in fixture[1]:
                with fixture[0]() as crud:
                    crud.insert(**row)


if __name__ == '__main__':

    user_input = None
    while user_input not in ('y', 'Y', 'n', 'N', ''):
        user_input = input('Do you want to drop all tables and reload the fixtures? (Y/n): ')
    if user_input in ('y', 'Y', ''):
        engine = Database().get_engine()
        metadata.drop_all(engine)
        metadata.create_all(engine)
        LoadFixtures().load()
    else:
        print('Exited without making any changes')
