"""
This is creates a pytest fixture.
"""
import pytest
from my_app import create_app


@pytest.fixture
def client():
    """This function creates a test client"""
    app = create_app()
    test_client = app.test_client()
    ctx = app.app_context()
    ctx.push()

    yield test_client

    ctx.pop()
