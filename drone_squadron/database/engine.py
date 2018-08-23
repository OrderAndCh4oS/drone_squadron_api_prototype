import os

from sqlalchemy import create_engine

if "PYTEST" in os.environ:
    engine = create_engine('sqlite:///drones_test.db')
else:
    engine = create_engine('sqlite:///drones.db')
