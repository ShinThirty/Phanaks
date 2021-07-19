from flask import Flask
from . import api_credentials_provider


def create_app(test_config=None) -> Flask:
    """Main entry point of the service. The application factory is responsible for
    creating and confguring the flask app. It also defines a http ping endpoint and registers blueprints.

    Returns:
        Flask: the flask app
    """
    app = Flask(__name__, instance_relative_config=True)
    if test_config:
        app.config.from_mapping(test_config)
    else:
        app.config.from_mapping(
            GIPHY_API_KEY=api_credentials_provider.resolve_credentials()
        )

    @app.route("/ping")
    def ping():
        return "OK"

    from . import search

    app.register_blueprint(search.bp)

    return app
