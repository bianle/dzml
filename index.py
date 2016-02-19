import web
from shortUrl import app_su,getUrl
web.config.debug = False       
urls = (
	'/','index',
        '/s',app_su,
         '/(.*)','redirect',
        '/(.*).html','staticHtml'
    
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
	if u.find('http://')==-1 and u.find("https://")==-1:
		u='http://'+u
        raise web.seeother(u)

class staticHtml:
	def GET(self,key):
		print key

		render = web.template.render('templates')
		mtd = getattr(render,key)
		return mtd()

if __name__ == "__main__":
    app.run()
