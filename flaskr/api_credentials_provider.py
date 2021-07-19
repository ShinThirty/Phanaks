import os


def resolve_credentials() -> str:
    """Resolves the API credentials by reading GIPHY_API_KEY environment variable.

    Returns:
        str: the API key from parsing the credentials profile
    """
    api_key = os.getenv("GIPHY_API_KEY")
    if api_key:
        return api_key
    else:
        raise RuntimeError(
            "Failed to read API key. Did you forget to set GIPHY_API_KEY environment variable?"
        )
