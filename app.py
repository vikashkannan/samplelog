from flask import Flask
import log_helper
app = Flask(__name__)
log = log_helper.get_logger(__name__)


@app.route("/")
def index():
    return "Hello, Azure World"
