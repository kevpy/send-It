"""
This is creates a pytest fixture.
"""
import pytest
from ... import create_app
from ...db.db_config import destroy_tables


@pytest.fixture(scope='session')
def client():
    app = create_app('testing')
    test_client = app.test_client()
    yield test_client
    destroy_tables()
