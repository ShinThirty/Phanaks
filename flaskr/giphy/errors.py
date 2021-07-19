from flask.wrappers import Response


class GiphyAPIError(Exception):
    """Raised when requests to Giphy API are not successful"""

    def __init__(
        self,
        r: Response,
        message="Giphy API request is reported as not successful",
    ) -> None:
        super().__init__(f"{message}: Error {r.status_code}")
