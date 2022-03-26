import pytest
from httpx import Client

from server.wsgi import app


@pytest.fixture
def client():
    with Client(app=app, base_url="http://test") as client_app:
        yield client_app
