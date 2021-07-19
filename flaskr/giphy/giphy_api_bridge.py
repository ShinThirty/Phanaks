from flaskr.giphy.entities import SearchResult
from flaskr.giphy.errors import GiphyAPIError
from flask import current_app
import requests

api_url = "api.giphy.com/v1"


def search_gif(api_key: str, term: str, limit: int) -> SearchResult:
    """Search gifs and returns the results.

    Args:
        api_key (str): the api key used to make the request to GIPHY
        term (str): the term used for the search
        limit (int): the maximum number of objects to return

    Raises:
        RuntimeError: when status code of the http request is not successful

    Returns:
        Any: the search result
    """
    params = {"api_key": api_key, "q": term, "limit": limit}
    url = f"https://{api_url}/gifs/search"

    current_app.logger.info(f"Starting requests to {url}")
    r = requests.get(url, params=params)
    current_app.logger.info(f"Finished request to {url}")
    if 200 <= r.status_code < 300:
        return SearchResult(r.json())
    else:
        raise GiphyAPIError(r)
