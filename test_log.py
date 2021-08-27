from log_helper import get_logger, log_setup

log = get_logger(__name__)


def test_logger():
    log_setup()
    log.debug('Test Log Debug')
    log.info('Test Log Info')
    log.warning('Test Log Warning')
    log.error('Test Log Error')

    try:
        c = 1 / 0
    except Exception as e:
        log.exception('Test Log Exception')

    log.critical('Test Log Critical')
