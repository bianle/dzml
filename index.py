import web
from shortUrl import app_su
web.config.debug = False       
urls = (
	'/','index',
    '/s',app_su
)
app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'count': 0})
class index:
	def GET(self):
		render = web.template.render('templates')
		return render.index()

if __name__ == "__main__":
    app.run()
