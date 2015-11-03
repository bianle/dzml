
from index import app
# local
if __name__ == "__main__":
    app.run()
else:
	# SAE
	import sae,os,sys
	root = os.path.dirname(__file__) 
	sys.path.insert(0, os.path.join(root, 'site-packages')) 
	app = app.wsgifunc()
	application = sae.create_wsgi_app(app)