from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Float, Enum, func, DateTime

from drone_squadron.database.engine import engine
from drone_squadron.enums import Status

metadata = MetaData()

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String(80)),
    Column('password', String(128)),
    Column('created_at', DateTime(timezone=True), server_default=func.now()),
    Column('updated_at', DateTime(timezone=True), onupdate=func.now())
)

squadron = Table(
    'squadron',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user', ForeignKey('user.id')),
    Column('name', String(80)),
    Column('scrap', Integer(), default=1000),
    Column('created_at', DateTime(timezone=True), server_default=func.now()),
    Column('updated_at', DateTime(timezone=True), onupdate=func.now())
)

drone = Table(
    'drone',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(40)),
    Column('kills', Integer, default=0),
    Column('missions', Integer, default=0),
    Column('value', Integer, default=0),
    Column('squadron', ForeignKey('squadron.id')),
    Column('weapon', ForeignKey('weapon.id')),
    Column('gimbal', ForeignKey('gimbal.id')),
    Column('scanner', ForeignKey('scanner.id')),
    Column('steering', ForeignKey('steering.id')),
    Column('thruster', ForeignKey('thruster.id')),
    Column('status', ForeignKey('status.id'), default=0),
    Column('created_at', DateTime(timezone=True), server_default=func.now()),
    Column('updated_at', DateTime(timezone=True), onupdate=func.now()),
)

price = Table(
    'price',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('item', String(12)),
    Column('related_id', Integer),
    Column('scrap', Integer, default=0)
)

weapon = Table(
    'weapon',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(12)),
    Column('fire_rate', Float),
    Column('round_type', ForeignKey('round_type.id')),
)

round_type = Table(
    'round_type',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(12)),
    Column('speed', Float),
    Column('radius', Float),
    Column('colour', String(12)),
    Column('damage', Float),
)

gimbal = Table(
    'gimbal',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(12)),
    Column('angle', Integer),
    Column('turning_speed', Float),
)

scanner = Table(
    'scanner',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(12)),
    Column('radius', Integer),
)

steering = Table(
    'steering',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(12)),
    Column('turning_speed', Float),
)

thruster = Table(
    'thruster',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(12)),
    Column('thrust_power', Float),
)

status = Table(
    'status',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('value', Enum(Status))
)

if __name__ == '__main__':
    # Todo: implement alembic migrations: pip install alembic

    user_input = None
    while user_input not in ('y', 'Y', 'n', 'N', ''):
        user_input = input('Do you want to drop all tables and recreate the schema? (Y/n): ')
    if user_input in ('y', 'Y', ''):
        metadata.drop_all(engine)
        metadata.create_all(engine)
    else:
        print('Exited without making any changes')
