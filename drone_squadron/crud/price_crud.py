from abc import ABCMeta

from drone_squadron.crud.base_crud import BaseCrud
from drone_squadron.schema import price


class PriceCrud(BaseCrud, metaclass=ABCMeta):

    def __init__(self, connection=None):
        super().__init__(price, connection)

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
