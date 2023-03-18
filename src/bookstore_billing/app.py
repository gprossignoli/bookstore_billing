from flask import Flask

from bookstore_billing.infrastructure.api.cli_blueprint import cli_commands
from bookstore_billing.settings import SECRET_KEY


def create_app() -> Flask:
	app = Flask(__name__)
	app.config["SECRET_KEY"] = SECRET_KEY

	app.register_blueprint(blueprint=cli_commands)
	return app


if __name__ == '__main__':
	app = create_app()
	app.run(host="0.0.0.0", port=8002)
