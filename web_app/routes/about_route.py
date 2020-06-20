from flask import Blueprint


about_route = Blueprint('about_route', __name__)

@about_route.route('/about')
def about():
    return 'deploy worked'