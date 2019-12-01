from sqlalchemy import select

from drone_squadron.crud.base_crud import BaseCrud
from drone_squadron.crud.price_crud import PriceCrud
from drone_squadron.crud.squadron_crud import SquadronCrud
from drone_squadron.schema import drone, weapon, steering, thruster, gimbal, scanner, status
from enums.status import Status


class DroneCrud(BaseCrud):
    def __init__(self, connection=None):
        super().__init__(drone, connection)
        self.squadron = SquadronCrud(self.connection)
        self.price = PriceCrud(self.connection)

    def select_by_id(self, item_id):
        return self.connection.execute(
            select([
                drone.c.id,
                drone.c.name,
                drone.c.kills,
                drone.c.missions,
                drone.c.value,
                weapon.c.name.label('weapon_name'),
                gimbal.c.name.label('gimbal_name'),
                thruster.c.name.label('thruster_name'),
                steering.c.name.label('steering_name'),
                scanner.c.name.label('scanner_name'),
                status.c.value.label('status_value')
            ])
                .select_from(drone.join(weapon)
                             .join(gimbal)
                             .join(thruster)
                             .join(steering)
                             .join(scanner)
                             .join(status, drone.c.status == status.c.id))
                .where(drone.c.id == item_id)
        )

    def insert(self, **kwargs):
        return self.connection.execute(
            drone.insert(),
            weapon=kwargs.pop('weapon') if 'weapon' in kwargs else 1,
            gimbal=kwargs.pop('gimbal') if 'gimbal' in kwargs else 1,
            thruster=kwargs.pop('thruster') if 'thruster' in kwargs else 1,
            steering=kwargs.pop('steering') if 'steering' in kwargs else 1,
            scanner=kwargs.pop('scanner') if 'scanner' in kwargs else 1,
            status=kwargs.pop('status') if 'status' in kwargs else 1,
            **kwargs
        )

    def update(self, **kwargs):
        # Todo squadron should not be in kwargs to begin with refactor to remove
        if 'squadron' in kwargs.keys():
            kwargs.pop('squadron')
        item_id = kwargs.pop('item_id')

        return self.connection.execute(
            drone.update().where(drone.c.id == item_id),
            **kwargs
        )

    def select_by_squadron_id(self, squadron_id):
        return self.connection.execute(
            select([
                drone.c.id,
                drone.c.name,
                drone.c.kills,
                drone.c.missions,
                drone.c.value,
                weapon.c.name.label('weapon_name'),
                gimbal.c.name.label('gimbal_name'),
                thruster.c.name.label('thruster_name'),
                steering.c.name.label('steering_name'),
                scanner.c.name.label('scanner_name'),
                status.c.value.label('status_value')
            ])
                .select_from(drone.join(weapon)
                             .join(gimbal)
                             .join(thruster)
                             .join(steering)
                             .join(scanner)
                             .join(status, drone.c.status == status.c.id))
                .where(drone.c.squadron == squadron_id)
        )


if __name__ == '__main__':
    with DroneCrud() as crud:
        result = crud.insert(
            name='Drone One',
            squadron=1
        )
        last_id = result.inserted_primary_key[0]

    with DroneCrud() as crud:
        result = crud.select()
        rows = result.fetchall()
        print("Select:", rows)

    with DroneCrud() as crud:
        result = crud.select_by_squadron_id(1)
        rows = result.fetchall()
        print("Select:", rows)

    with DroneCrud() as crud:
        result = crud.update(
            item_id=last_id,
            name="Test",
            weapon=1,
            squadron=1,
        )
        updated_params = result.last_updated_params()
        print("Update:", updated_params)

    with DroneCrud() as crud:
        result = crud.delete(item_id=last_id)
