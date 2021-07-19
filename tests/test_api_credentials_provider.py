from flaskr import api_credentials_provider
from pytest import raises


def test_no_credentials(remove_api_key):
    """When no credentials are given web server should raise error.

    Args:
        remove_api_key ([type]): remove_api_key fixture
    """
    with raises(
        RuntimeError,
        match="Failed to read API key. Did you forget to set GIPHY_API_KEY environment variable?",
    ):
        api_credentials_provider.resolve_credentials()
