import os,sys
root = os.path.dirname(__file__) 
sys.path.insert(0, os.path.join(root, 'site-packages/short_url-1.2.1-py2.7.egg'))

from index import app

# local
if __name__ == "__main__":
    app.run()
else:
	# SAE
	import sae
	app = app.wsgifunc()
	application = sae.create_wsgi_app(app)