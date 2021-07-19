from requests.models import Response
from flaskr.giphy.errors import GiphyAPIError
import json
from flaskr.giphy.entities import SearchResult


def test_search_5_results(client, mocker):
    """Returns all 5 results"""
    with open("tests/data/giphy_response_5_results.json") as input_data:
        r_json = json.load(input_data)
        mocker.patch(
            "flaskr.search.giphy_api_bridge.search_gif",
            return_value=SearchResult(r_json),
        )
    response = client.get("/search/cat")
    response_json = json.loads(response.data)
    data = response_json["data"]

    assert len(data) == 5


def test_search_2_results(client, mocker):
    """Returns empty result when total result number is less than 5"""
    with open("tests/data/giphy_response_2_results.json") as input_data:
        r_json = json.load(input_data)
        mocker.patch(
            "flaskr.search.giphy_api_bridge.search_gif",
            return_value=SearchResult(r_json),
        )
    response = client.get("/search/cat")
    response_json = json.loads(response.data)
    data = response_json["data"]

    assert len(data) == 0


def test_search_6_results(client, mocker):
    """Returns 5 results when total result number is more than 5"""
    with open("tests/data/giphy_response_6_results.json") as input_data:
        r_json = json.load(input_data)
        mocker.patch(
            "flaskr.search.giphy_api_bridge.search_gif",
            return_value=SearchResult(r_json),
        )
    response = client.get("/search/cat")
    response_json = json.loads(response.data)
    data = response_json["data"]

    assert len(data) == 5


def test_search_handle_giphy_api_error(client, mocker):
    """Returns 500 response when Giphy API fails to respond successfully"""
    r = Response()
    r.status_code = 500
    mocker.patch(
        "flaskr.search.giphy_api_bridge.search_gif", side_effect=GiphyAPIError(r)
    )

    response = client.get("/search/cat")

    assert response.status_code == 500
