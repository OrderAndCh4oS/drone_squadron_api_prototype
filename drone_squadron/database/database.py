import os

from sqlalchemy import create_engine


class Database:
    def __init__(self):
        if "PYTEST" in os.environ:
            self.engine = create_engine(self._make_path('drones_test.db'))
        else:
            self.engine = create_engine(self._make_path('drones.db'))

    def _make_path(self, database):
        db_path = os.path.join(os.path.dirname(__file__), database)
        return 'sqlite:///{}'.format(db_path)

    def get_connection(self):
        return self.engine.connect()

    def get_engine(self):
        return self.engine
