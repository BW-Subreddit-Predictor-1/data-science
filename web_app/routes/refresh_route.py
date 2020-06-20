import sqlite3
import praw, json
from dotenv import load_dotenv
import os
from flask import Blueprint, jsonify, request, render_template, flash, redirect

from web_app.models import db, Subreddit, Thread, parse_records

load_dotenv()

REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
REDDIT_USER_AGENT = os.getenv('REDDIT_USER_AGENT')

refresh_route = Blueprint('refresh_route', __name__)

@refresh_route.route('/refresh')
def refresh_data():
    
    test = db.session.execute('SELECT * FROM subreddit').fetchall()  
    subreddit_list = [x[1] for x in test]
    print(subreddit_list)
    
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT)

    for each in subreddit_list:
        submissions = reddit.subreddit(each).hot(limit=200)
        print(f'\n{each}')
        
        for submission in submissions:
            db_thread = Thread.query.get(submission.id) or Thread(id=submission.id)
            db_thread.title = submission.title
            db_thread.body = submission.selftext
            db_thread.upvotes = submission.score
            db_thread.subreddit = Subreddit.query.filter_by(subreddit=each).first().id
            db.session.add(db_thread)
            
    db.session.commit()
    return 'data refreshed'

