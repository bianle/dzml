import web
import json
from orm import *
import short_url  
urls = ('/', 'index',
        '/url/(.*)','url'
        )

app_su = web.application(urls, locals())
session = web.session.Session(app_su, web.session.DiskStore('sessions'))

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
        key = 'jy7yj'
        pk = short_url.decode_url(key)
        return pk
    ## update
    def PUT(self,key):
        
        return 1
def addUrl(param):
    print 'addUrl'
    url = param.u
    u = Url(url=url)
    k = u.save()
    rst = short_url.encode_url(k)
    print rst
    rst =  url+' --> '+'http://2le.me/'+ rst 
    print rst
    return rst
def updateUrl(param):
    pass