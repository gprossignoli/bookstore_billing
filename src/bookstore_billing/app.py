from flask import Flask

from bookstore_billing.settings import SECRET_KEY


def create_app() -> Flask:
	app = Flask(__name__)
	app.config["SECRET_KEY"] = SECRET_KEY

	return app


if __name__ == '__main__':
	app = create_app()
	app.run(host="0.0.0.0", port=8002)
