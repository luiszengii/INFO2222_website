import bottle
app = application = bottle.Bottle()

@app.route('/helloTTT')
def show_index():
    '''
    The front "index" page
    '''
    return 'Hello hhhh world!'


if __name__ == '__main__':
    bottle.run()
