# web_app/__init__.py

from flask import Flask
from dotenv import load_dotenv
import os

from web_app.models import db, migrate


load_dotenv()
DATABASE_URI = "sqlite:///bwpt_phsp1_ds.db"

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    db.init_app(app)
    migrate.init_app(app, db)

    return app

if __name__ == '__main__':
    my_app = create_app()
    my_app.run(debug=True)
