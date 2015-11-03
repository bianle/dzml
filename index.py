import web
web.config.debug = False       
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'count': 0})

class hello:        
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()
