from flask import Blueprint


refresh_route = Blueprint('about_route', __name__)

@refresh_route.route('/about')
def about():
    return 'deploy worked'