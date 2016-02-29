# -*- coding: utf-8 -*-

import web
from shortUrl import app_su,getUrl
web.config.debug = False       
urls = (
	'/','index',
        '/s',app_su,
        '/addrbook','addrbook',
        '/(.*).html','staticHtml',
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
	if u.find('http://')==-1 and u.find("https://")==-1:
		u='http://'+u
        raise web.seeother(u)

class addrbook:
        def POST(self):
                d = web.input()
                name = d.name
                if name =="":
                        return "name is null"
                from mysql import getDb
                rst = getDb().query("select count(*) CT from py_addrbook where name = $name",vars=locals())
                if rst[0].CT >0:
                        return "Sorry!duplicate name!"
                getDb().insert('py_addrbook',name=d.name,mobile=d.mobile,addr=d.addr,qq=d.qq,wechat=d.wechat,other=d.other)
                return 'Success!Thanks!'
        def GET(self):
                d = web.input()
                name = d.name
                if name =="":
                        return ""
                from mysql import getDb
                import json
                rst = getDb().query("select * from py_addrbook where name=$name",vars=locals())
                return json.dumps(package(rst))

class staticHtml:
        def GET(self,key):
		print key

		render = web.template.render('templates')
		mtd = getattr(render,key)
		return mtd()

def package(rst):
    lst = []
    for rcd in rst:
        lst.append(dict(rcd))
    return lst

if __name__ == "__main__":
    app.run()
