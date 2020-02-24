""" Main flask app """

import os

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# Make db importable

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    """Create flask app

    Returns:
        Flask -- current flask app
    """

    app = Flask(__name__)
    CORS(app)

    # Initialize database
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv(
        "SQLALCHEMY_TRACK_MODIFICATIONS")

    db.init_app(app)
    migrate.init_app(app, db)

    # Setup API Blueprints
    from .api.customer.route import customer
    app.register_blueprint(customer, url_prefix='/customer')

    return app
