from flask import Flask, request, send_from_directory

from wardrobe.entrypoints.flask_app.config import config
from wardrobe.entrypoints.flask_app.message_bus import bus


def create_app(config_name="default"):
    app = Flask(__name__)
    app_config = config[config_name]
    app.config.from_object(app_config)
    app_config.init_app(app)

    init_blueprint(app)

    return app


def init_blueprint(app):
    @app.route("/", methods=["GET"])
    def index():
        return "index"

    @app.route("/robots.txt", methods=["GET"])
    def robots_txt():
        return send_from_directory(app.static_folder, request.path[1:])
