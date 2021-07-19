from flask.wrappers import Response


class GIFData:
    """GIF data class, storing gif id and gif url.
    """
    def __init__(self, item) -> None:
        self.gif_id = item["id"]
        self.url = item["url"]


class SearchResult:
    """GIF search result construct. Contains one field "data" which is a collection of GIFData.
    """
    def __init__(self, r_json) -> None:
        data = r_json["data"]
        self.data = []

        if len(data) >= 5:
            self.data = [GIFData(item) for item in data[:5]]
