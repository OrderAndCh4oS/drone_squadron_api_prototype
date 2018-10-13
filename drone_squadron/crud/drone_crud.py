from sqlalchemy import select

from crud.price_crud import PriceCrud
from crud.squadron_crud import SquadronCrud
from drone_squadron.crud.base_crud import BaseCrud
from drone_squadron.schema import drone, weapon, steering, thruster, gimbal, scanner


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
                scanner.c.name.label('scanner_name')
            ])
                .select_from(drone.join(weapon)
                             .join(gimbal)
                             .join(thruster)
                             .join(steering)
                             .join(scanner))
                .where(drone.c.id == item_id)
        )

    def insert(self, **kwargs):
        drone_cost = 50
        squadron_id = kwargs.pop('squadron')
        item_cost = self.calculate_cost(kwargs)
        cost = item_cost + drone_cost
        self.squadron.spend_scrap(squadron_id, cost)
        return self.connection.execute(
            drone.insert(),
            squadron=squadron_id,
            weapon=kwargs.get('weapon', 1),
            gimbal=kwargs.get('gimbal', 1),
            thruster=kwargs.get('thruster', 1),
            steering=kwargs.get('steering', 1),
            scanner=kwargs.get('scanner', 1),
            value=cost,
            **kwargs
        )

    def update(self, **kwargs):
        squadron_id = kwargs.pop('squadron')
        item_id = kwargs.pop('item_id')
        cost = self.calculate_cost(kwargs)
        self.squadron.spend_scrap(squadron_id, cost)
        # Todo: calculate and update drone value
        return self.connection.execute(
            drone.update().where(drone.c.id == item_id),
            **kwargs
        )

    def calculate_cost(self, kwargs):
        cost = 0
        item_types = ('weapon', 'gimbal', 'scanner', 'thruster', 'steering')
        for item_type in item_types:
            if item_type in kwargs:
                price = self.price.select_by_type_and_related_id(item_type, kwargs.get(item_type))
                cost = cost + price.fetchone().scrap
        return cost

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
                scanner.c.name.label('scanner_name')
            ])
                .select_from(drone.join(weapon)
                             .join(gimbal)
                             .join(thruster)
                             .join(steering)
                             .join(scanner))
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
            squadron=1
        )
        updated_params = result.last_updated_params()
        print("Update:", updated_params)

    with DroneCrud() as crud:
        result = crud.delete(item_id=last_id)
