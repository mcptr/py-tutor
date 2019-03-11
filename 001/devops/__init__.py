import logging
import json
from . import db


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


def load_clusters(path):
    return db.load_servers(path)


def display(data):
    print(json.dumps(data, indent=4))
