import logging

from flask import current_app, Blueprint

from aginghub.repository import Repository

home_routes = Blueprint('Home Routes', __name__, url_prefix='/')

@home_routes.route('/')
def home_route():
    logging.info('Request received to /')
    return current_app.send_static_file('index.html')

@home_routes.route('/api/home')
def home_api_route():
    logging.info('Request received to /api/home')
    repo = Repository()
    return repo.get_aging_counter()