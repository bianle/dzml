import web
import json
from orm import *
import short_url  
urls = ('/', 'index',
        '/url/(.*)','url'
        )

app_su = web.application(urls, locals())

class index:
    def GET(self):
        return 'short!'

class url:
    ## create
    def POST(self,key):
        print web.input()
        return addUrl(web.input())
    ## delete
    def DELETE(self,key):
        return 'dlt'
    ## read
    def GET(self,key):
        return getUrl(key)
    ## update
    def PUT(self,key):
        
        return 1
def addUrl(param):
    print 'addUrl'
    url = param.u
    hs = hash(url)
    rst = Url.find(what='id',where='hash='+str(hs))
    try:
        k = rst[0].id
    except:
        u = Url(url=url)
        k = u.save()
    rst = short_url.encode_url(k)
    print rst
    return rst
def getUrl(key):
    pk = short_url.decode_url(key)
    rs = Url.find(what='url',where='id=$pk',vars=locals())
    rcd = rs[0]
    return rcd.url
def updateUrl(param):
    pass
