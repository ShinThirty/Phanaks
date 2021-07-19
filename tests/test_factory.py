from flaskr import create_app
import os


def test_config(api_key):
    """Testing configuration should only be in effect when TESTING is set to true.

    Args:
        api_key ([type]): api_key fixture
    """
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_ping(client):
    """Test ping health check.

    Args:
        client ([type]): client fixture
    """
    response = client.get("/ping")
    assert response.data == b"OK"
