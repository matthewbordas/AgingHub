import pytest
from flask import Flask

from aginghub import create_app
from aginghub.repository import Repository

@pytest.fixture
def test_app() -> Flask:
    yield create_app()
    repo = Repository()
    repo.clear_aging_counter()

@pytest.fixture
def test_client(test_app) -> Flask:
    return test_app.test_client()