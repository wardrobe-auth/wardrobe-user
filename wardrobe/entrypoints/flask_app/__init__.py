from flask import Flask, request

from wardrobe.domain import commands
from wardrobe.entrypoints.flask_app.message_bus import bus


def create_app():
    app = Flask(__name__)
    init_bp(app)

    return app


def init_bp(app):
    @app.route("/hello", methods=["GET"])
    def say_hello():
        cmd = commands.SayHelloCommand(name=request.args.get("name", "John"))
        resp = bus.handle(cmd)
        return resp
