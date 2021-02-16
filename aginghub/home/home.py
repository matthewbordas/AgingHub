import logging

from flask import Blueprint

from aginghub.repository import Repository

home_api = Blueprint('Home API', __name__, url_prefix='/api/home/')

@home_api.route('/')
def home_route():
    logging.info('Request received to /api/home/')
    repo = Repository()
    return repo.get_aging_counter()
