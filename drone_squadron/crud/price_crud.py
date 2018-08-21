from abc import ABCMeta

from drone_squadron.crud.base_crud import BaseCrud
from drone_squadron.schema import price


class PriceCrud(BaseCrud, metaclass=ABCMeta):

    def __init__(self, connection=None):
        super().__init__(price, connection)

    def update(self, item_id, scrap, type):
        return self.connection.execute(
            price.update()
                .where(price.c.related_id == item_id)
                .where(price.c.type == type)
            ,
            scrap=scrap
        )
