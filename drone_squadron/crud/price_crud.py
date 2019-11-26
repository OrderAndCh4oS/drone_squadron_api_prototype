from abc import ABCMeta

from sqlalchemy import select, union_all

from drone_squadron.crud.base_crud import BaseCrud
from drone_squadron.schema import price, weapon, gimbal, thruster, steering, scanner


class PriceCrud(BaseCrud, metaclass=ABCMeta):

    def __init__(self, connection=None):
        super().__init__(price, connection)

    def select(self):
        def select_statement(item, item_type):
            return select([
                price.c.item,
                price.c.scrap,
                item.c.name,
                item.c.id.label('item_id')
            ]).select_from(
                price.join(item, price.c.related_id == item.c.id)
            ).where(price.c.item == item_type)

        statement = union_all(
            select_statement(weapon, 'weapon'),
            select_statement(gimbal, 'gimbal'),
            select_statement(thruster, 'thruster'),
            select_statement(steering, 'steering'),
            select_statement(scanner, 'scanner'),
        )

        return self.connection.execute(statement)

    def select_by_type_and_related_id(self, item_type, related_id):
        return self.connection.execute(
            price.select()
                 .where(price.c.related_id == related_id)
                 .where(price.c.item == item_type)
        )

    def update(self, item_id, scrap, item_type):
        return self.connection.execute(
            price.update()
                 .where(price.c.related_id == item_id)
                 .where(price.c.type == item_type)
            ,
            scrap=scrap
        )
