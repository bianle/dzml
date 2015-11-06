import web
from shortUrl import app_su,getUrl
web.config.debug = False       
urls = (
	'/','index',
        '/s',app_su,
         '/(.*)','redirect'
    
)
app = web.application(urls, globals())
'''
try:
        from sae.ext.storage import monkey
        monkey.patch_all()
        session_root = '/s/session/'
except:
        session_root = 'session/'
session = web.session.Session(app, web.session.DiskStore(session_root))
'''
class index:
	def GET(self):
		render = web.template.render('templates')
		return render.index()

class redirect:
    def GET(self,key):
        key = key.replace('/','')
        u = getUrl(key)
        raise web.seeother(u)
if __name__ == "__main__":
    app.run()
