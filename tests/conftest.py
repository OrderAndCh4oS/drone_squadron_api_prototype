import pytest


@pytest.fixture(scope="module")
def connection():
    from sqlalchemy import create_engine
    from drone_squadron.schema import metadata
    engine = create_engine('sqlite:///drones_test.db')
    metadata.create_all(engine)
    connection = engine.connect()
    yield connection
    connection.close()
    metadata.drop_all(engine)
