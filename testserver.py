import bottle

@bottle.get('/')
def getmain():
    return bottle.static_file('index.html', root='.')

@bottle.get('/fonts/alegreya/<filename>')
def getAlegreya(filename):
    return bottle.static_file(filename, root='./fonts/alegreya')

@bottle.get('/fonts/greatvibes/<filename>')
def getAlegreya(filename):
    return bottle.static_file(filename, root='./fonts/greatvibes')

@bottle.get('/<filename>')
def getstyles(filename):
    if '.' not in filename:
        filename = filename + '.html'
    return bottle.static_file(filename, root='.')

@bottle.get('/clickslideshow/<filename>')
def slideshow(filename):
    return bottle.static_file(filename, root='./clickslideshow')

@bottle.get('/chapelTop/<filename>')
def chapelTop(filename):
    return bottle.static_file(filename, root='./chapelTop')

@bottle.get('/chapelManual/<filename>')
def chapelTop(filename):
    return bottle.static_file(filename, root='./chapelManual')

@bottle.get('/topslideshow/<filename>')
def topslideshow(filename):
    return bottle.static_file(filename, root='./topslideshow')

@bottle.get('/reviewPhotos/<filename>')
def topslideshow(filename):
    return bottle.static_file(filename, root='./reviewPhotos')

@bottle.get('/localPhotos/<filename>')
def topslideshow(filename):
    return bottle.static_file(filename, root='./localPhotos')

@bottle.get('/roomPhotos/<filename>')
def topslideshow(filename):
    return bottle.static_file(filename, root='./roomPhotos')

bottle.run(host='localhost', port=3000, debug=True, server='paste')
