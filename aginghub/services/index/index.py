import logging

from flask import Blueprint

#from aginghub.repository import Repository

index_api = Blueprint('Index API', __name__, url_prefix='/')

@index_api.route('/')
def index_route() -> str:
    logging.info('Request received to /')
    return 'Welcome to AgingHub. Check back soon for more!'
    #repo = Repository()
    #return repo.get_aging_counter()
