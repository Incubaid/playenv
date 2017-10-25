
from . import app, logger


@app.task
def start():
    logger.info('start')
    return "carrot.start"


@app.task
def add(nr=1):
    return "carrot.add:%s" % nr
