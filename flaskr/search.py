import json
from flaskr.giphy.errors import GiphyAPIError
from flask import Blueprint, current_app
from flaskr.giphy import giphy_api_bridge

bp = Blueprint("search", __name__)


@bp.route("/search/<term>")
def search(term: str):
    """Search GIFs with given term. Returns 5 results if we find 5 or
    more results from Giphy and no results if we find less.

    Args:
        term (str): search terms

    Returns:
        str: a serialized representaion of the search result.
    """
    api_key = current_app.config["GIPHY_API_KEY"]
    search_result = giphy_api_bridge.search_gif(api_key, term, 5)
    return json.dumps(search_result, default=lambda o: o.__dict__, indent=2)


@bp.errorhandler(GiphyAPIError)
def handle_api_error(e):
    """Returns 500 internal server error when Giphy API doesn't respond successfully.
    """
    return f"Failed to call Giphy API: {e}", 500
