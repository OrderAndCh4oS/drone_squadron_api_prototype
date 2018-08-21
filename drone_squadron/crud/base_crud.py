from abc import ABCMeta

from drone_squadron.database.engine import engine


class BaseCrud(metaclass=ABCMeta):
    connection = None

    def __init__(self, table, connection=None):
        self.table = table
        self.action = None
        self.results = None
        self.connection = connection
        self.connect()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def connect(self):
        if self.connection is None:
            self.connection = engine.connect()

    def select(self):
        return self.connection.execute(self.table.select())

    def select_by_id(self, item_id):
        return self.connection.execute(self.table.select().where(self.table.c.id == item_id))

    def insert(self, **kwargs):
        return self.connection.execute(
            self.table.insert(), **kwargs
        )

    def update(self, **kwargs):
        item_id = kwargs.pop('item_id')
        return self.connection.execute(
            self.table
                .update()
                .where(self.table.c.id == item_id),
            **kwargs
        )

    def delete(self, item_id):
        return self.connection.execute(
            self.table.delete().where(self.table.c.id == item_id)
        )

    def execute(self, action, **kwargs):
        return self.connection.execute(action, **kwargs)

    def close(self):
        self.connection.close()
