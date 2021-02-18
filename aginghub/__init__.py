import logging
from logging.config import dictConfig
import os
import pathlib

from flask import Flask
import yaml

from aginghub.home import home_routes
from .repository import Repository

def create_app() -> Flask:
    configure_logger()
    app = Flask(__name__, static_folder='./dist', static_url_path='/')
    app.register_blueprint(home_routes)
    repo = Repository()
    repo.load_aging_counter(repo.get_aging_counter_path())

    logging.info('App created successfully')
    return app

def configure_logger() -> None:
    path = pathlib.Path(__file__).parent.absolute()
    with open(f'{path}/../logging.conf.yml') as logging_conf:
        dictConfig(yaml.safe_load(logging_conf))