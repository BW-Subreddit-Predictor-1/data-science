# web_app/__init__.py

from flask import Flask
from dotenv import load_dotenv
import os

from web_app.models import db, migrate
from web_app.routes.refresh_route import refresh_route
from web_app.routes.about_route import about_route

load_dotenv()
DATABASE_URI = os.getenv(DATABASE_URL)

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(refresh_route)
    app.register_blueprint(about_route)

    return app

if __name__ == '__main__':
    my_app = create_app()
    my_app.run(debug=True)
