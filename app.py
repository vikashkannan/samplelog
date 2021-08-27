import log_helper
from test_log import test_logger
from test_log_01 import test_logger_01
import os

from flask import Flask, render_template

ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

log = log_helper.get_logger(__name__)
log_helper.log_setup()


def main():
    log.info('Test Info')
    test_logger()
    pass


@app.route('/', methods=['GET'])
def index():
    test_logger()
    return "Welcome to Azure"


@app.route('/data')
def names():
    test_logger()
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return data
