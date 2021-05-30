import sys
from bottle import run
import bottle
import model
import view
import controller

host = '10.86.227.4'
port = 8080
debug = True
reloader=True

app = application = bottle.default_app()

if __name__ == '__main__':
    run(host=host, port=port, debug=False)
