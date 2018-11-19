"""
This is creates a pytest fixture.
"""
import pytest
from ... import create_app
from ...db.db_config import destroy_tables


@pytest.fixture
def client():
    app = create_app('testing')
    yield app
    destroy_tables()
