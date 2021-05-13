'''
    This is a file that configures how your server runs
    You may eventually wish to have your own explicit config file
    that this reads from.

    For now this should be sufficient.

    Keep it clean and keep it simple, you're going to have
    Up to 5 people running around breaking this constantly
    If it's all in one file, then things are going to be hard to fix

    If in doubt, `import this`
'''

#-----------------------------------------------------------------------------

import sys
import bottle
from bottle import run

import model
import view
import controller

if __name__ == "__main__":
    app = bottle.default_app()
    
    host = '10.86.227.4'
    port = 8080
    debug = True
    reloader = True

    run(app=app, host=host, port=port, debug=debug, reloader=reloader)

else:
    application = bottle.default_app()
