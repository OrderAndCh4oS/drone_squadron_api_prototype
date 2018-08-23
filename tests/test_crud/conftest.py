import pytest


@pytest.fixture(scope="session")
def setup():
    from drone_squadron.database.database import Database
    from drone_squadron.schema import metadata
    engine = Database().get_engine()
    metadata.drop_all(engine)
    metadata.create_all(engine)
    yield
    metadata.drop_all(engine)
