from flask.app import Flask
import pytest
from flaskr import create_app
import os

# Fixture defined here can be reference by test methods with name matching.
# Placing the name of a fixture in the argument list of a test method will cause the fixture get executed when execuing that test method.

@pytest.fixture
def app():
    app = create_app({"TESTING": True, "GIPHY_API_KEY": "dummy_api_key"})
    yield app


@pytest.fixture
def client(app: Flask):
    return app.test_client()


@pytest.fixture
def runner(app: Flask):
    return app.test_cli_runner()


@pytest.fixture
def api_key():
    os.environ["GIPHY_API_KEY"] = "dummy_api_key"
    yield
    del os.environ["GIPHY_API_KEY"]


@pytest.fixture
def remove_api_key():
    del os.environ["GIPHY_API_KEY"]
