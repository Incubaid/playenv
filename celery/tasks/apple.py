
from . import app


@app.task
def start():
    return "apple.start"


@app.task
def add(nr=1):
    return "apple.add:%s" % nr
