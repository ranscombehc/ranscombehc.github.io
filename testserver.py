import bottle

@bottle.get('/')
def getmain():
    return bottle.static_file('index.html', root='.')

@bottle.get('/<filename>')
def getstyles(filename):
    if '.' not in filename:
        filename = filename + '.html'
    return bottle.static_file(filename, root='.')

@bottle.get('/chapelTop/<filename>')
def chapelTop(filename):
    return bottle.static_file(filename, root='./chapelTop')

@bottle.get('/chapelManual/<filename>')
def chapelTop(filename):
    return bottle.static_file(filename, root='./chapelManual')

@bottle.get('/localPhotos/<filename>')
def chapelTop(filename):
    return bottle.static_file(filename, root='./localPhotos')

bottle.run(host='localhost', port=3000, debug=True, server='paste')
