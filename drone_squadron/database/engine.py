import os

from sqlalchemy import create_engine

if "PYTEST" in os.environ:
    engine = create_engine('sqlite:////home/sarcoma/PycharmProjects/drone_squadron/tests/drones_test.db')
else:
    engine = create_engine('sqlite:////home/sarcoma/PycharmProjects/drone_squadron/drone_squadron/drones.db')
