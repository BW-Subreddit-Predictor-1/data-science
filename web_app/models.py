# models.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()

class Subreddit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subreddit = db.Column(db.String(128))

    def __repr__(self):
        return f'{self.subreddit}'

class Thread(db.Model):
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    title_embedding = db.Column(db.PickleType, nullable=True)
    body = db.Column(db.String, nullable=True)
    body_embedding = db.Column(db.PickleType, nullable=True)
    upvotes = db.Column(db.Integer)
    subreddit = db.Column(db.Integer, db.ForeignKey('subreddit.id'))

# thanks prof mike for showing us this code
def parse_records(database_records):
    """
    A helper method for converting a list of database record objects into a list of dictionaries, so they can be returned as JSON
    Param: database_records (a list of db.Model instances)
    Example: parse_records(User.query.all())
    Returns: a list of dictionaries, each corresponding to a record, like...
        [
            {"id": 1, "title": "Book 1"},
            {"id": 2, "title": "Book 2"},
            {"id": 3, "title": "Book 3"},
        ]
    """
    parsed_records = []
    for record in database_records:
        print(record)
        parsed_record = record.__dict__
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)
    return parsed_records