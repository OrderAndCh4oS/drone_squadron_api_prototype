from abc import ABCMeta

from drone_squadron.crud.base_crud import BaseCrud
from drone_squadron.crud.price_crud import PriceCrud


class ItemCrud(BaseCrud, metaclass=ABCMeta):

    def __init__(self, table, name, connection):
        super().__init__(table, connection)
        self.table_name = name
        self.price_crud = PriceCrud(self.connection)

    def insert(self, scrap=None, **kwargs):
        result = self.connection.execute(
            self.table.insert(),
            **kwargs
        )
        self.price_crud.insert(
            scrap=scrap,
            item=self.table_name,
            related_id=result.inserted_primary_key[0]
        )

        return result

    def update(self, item_id=None, scrap=None, **kwargs):
        result = self.connection.execute(
            self.table.update().where(self.table.c.id == item_id),
            **kwargs
        )
        if scrap:
            self.price_crud.update(
                item_id=item_id,
                scrap=scrap,
                type=self.table_name
            )
        return result
