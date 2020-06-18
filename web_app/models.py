# models.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()

class Subreddit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subreddit = db.Column(db.String(128))

class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    title_embedding = db.Column(db.PickleType)
    body = db.Column(db.String)
    body_embedding = db.Column(db.PickleType)
    upvotes = db.Column(db.Integer)
    subreddit = db.Column(db.Integer, db.ForeignKey('subreddit.id'))