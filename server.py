from flask import Flask,render_template
from flask_restplus import Resource, Api
import newspaper,json
app = Flask(__name__)
api = Api(app)

@api.route('/api/v1/get-articles/<string:site>')
@api.doc(params={'site':"Site name without http prefix Ex:ndtv.com"})
class Articles(Resource):
	def get(self,site):
		print site
		paper=newspaper.build("http://"+site)
		articles={}
		i=0
		for article in paper.articles:
			articles[i]=article.url
			i=i+1
		return {'articles':articles}

@api.route('/index')
class Home(Resource):
    def get(self):
        return {'hello': 'world'}


if __name__ == "__main__":
    app.run()
