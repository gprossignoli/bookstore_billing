from flask import Flask

from bookstore_billing.infrastructure.api.config.blueprints import register_blueprints
from bookstore_billing.infrastructure.api.config.db import configure_db
from bookstore_billing.settings import SECRET_KEY, db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY
    with app.app_context():
        register_blueprints(app)
        configure_db(app=app, db=db)

    return app


if __name__ == "__main__":
    flask_app = create_app()
    flask_app.run(host="0.0.0.0", port=8002)
