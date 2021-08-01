from flask import Flask
from routes import hello_world
import auth
import os


dir = os.path.abspath(os.path.dirname(__file__))


def create_app(config_filename=None):

    app = Flask(__name__)

    if not config_filename:
        config_filename = os.environ['APP_SETTINGS']

    app.config.from_object(config_filename)

    app.register_blueprint(hello_world.bp)
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return app.send_static_file('index.html'), 200

    return app


app = create_app()


if __name__ == '__main__':
    app.run()
