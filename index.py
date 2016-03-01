# -*- coding: utf-8 -*-

import web
from shortUrl import app_su,getUrl
web.config.debug = False       
urls = (
	'/','index',
        '/s',app_su,
        '/addrbook','addrbook',
        '/ab','ab',
        '/dl','download',
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
                        getDb().update('py_addrbook',name=d.name,mobile=d.mobile,addr=d.addr,qq=d.qq,wechat=d.wechat,other=d.other,where="name=$name",vars=locals())
                        return "Update Success!Thanks!"
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
class ab:
        def GET(self):
                from mysql import getDb
                rst = getDb().query("select * from py_addrbook ",vars=locals())
                render = web.template.render('templates')
                return render.ab(rst)

class download:
    def GET(self):
        from mysql import getDb
        rst = getDb().query("select * from py_addrbook ",vars=locals())
        addTxt = u'姓名,手机,现住址,QQ,微信,其他\n'
        for rcd in rst:
                addTxt+=rcd.name+","+rcd.mobile+","+rcd.addr+","+rcd.qq+","+rcd.wechat+","+rcd.other+"\n"
        import StringIO,codecs
        s = StringIO.StringIO()
        s.write(unicode(codecs.BOM_UTF8,"utf-8"))
        s.write(addTxt)
        s.seek(0)
        web.header("Content-Type","text/csv;charset=utf-8") #content-type需要根据实际的文件类型来指定
        web.header("Content-Disposition","attachment;filename=0411.csv")
        while True:
            c = s.read(2048)
            if c:
                yield c
            else:
                break
        
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
