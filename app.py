from flask import Flask
import log_helper
app = Flask(__name__)
log = log_helper.get_logger(__name__)

@app.route("/")
def index():
    log_helper.log_setup()
    log.debug('Test Log Debug')
    log.info('Test Log Info')
    log.warning('Test Log Warning')
    log.error('Test Log Error')
    return "Hello, Azure World"
