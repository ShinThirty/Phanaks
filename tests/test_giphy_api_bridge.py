from flaskr.giphy.errors import GiphyAPIError
from requests.models import Response
from pytest import raises

from flaskr.giphy import giphy_api_bridge


def mocked_requests_get_5_results(*args, **kwargs):
    """Generates the response with the local provisioned data which contains 5 GIF search results.
    """
    content = None
    with open("tests/data/giphy_response_5_results.json") as data_file:
        content = data_file.read()
    response = Response()
    response.status_code = 200
    response._content = str.encode(content)
    return response


def mocked_requests_get_500_response(*args, **kwargs):
    """Generates the response the 500 response code.
    """
    response = Response()
    response.status_code = 500
    return response


def test_search_gif(app, mocker):
    """Search GIF call should retain the results."""
    mocker.patch("requests.get", side_effect=mocked_requests_get_5_results)
    with app.app_context():
        search_result = giphy_api_bridge.search_gif("dummy_api_key", "cat", 5)

    assert len(search_result.data) == 5


def test_search_gif_error(app, mocker):
    """Search GIF call should raise GiphyAPIError when Giphy API responds with unsuccessful response."""
    mocker.patch("requests.get", side_effect=mocked_requests_get_500_response)
    with app.app_context():
        with raises(GiphyAPIError):
            giphy_api_bridge.search_gif("dummy_api_key", "cat", 5)
