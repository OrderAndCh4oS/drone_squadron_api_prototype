import pytest


@pytest.fixture(scope="session")
def setup():
    from drone_squadron.database.engine import engine
    from drone_squadron.schema import metadata
    metadata.create_all(engine)
    yield
    metadata.drop_all(engine)
