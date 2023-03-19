from flask import Flask

from bookstore_billing.infrastructure.api.admin_blueprint import admin_blueprint
from bookstore_billing.infrastructure.api.billing_blueprint import billing_blueprint
from bookstore_billing.infrastructure.api.cli_blueprint import cli_commands


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(blueprint=admin_blueprint)
    app.register_blueprint(blueprint=cli_commands)
    app.register_blueprint(blueprint=billing_blueprint)
