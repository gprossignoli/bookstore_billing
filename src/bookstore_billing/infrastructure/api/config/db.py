from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from bookstore_billing.settings import DB_URI


def configure_db(app: Flask, db: SQLAlchemy) -> None:
    # create the extension
    # configure the SQLite database, relative to the app instance folder
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    # initialize the app with the extension
    db.init_app(app)
    Migrate(app, db, compare_type=True)
    db.create_all()
