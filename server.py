from flask import Flask
from flask_restplus import Resource, Api
import newspaper,json,urllib
app = Flask(__name__)
api = Api(app)

@api.route('/api/v1/get-articles/<string:site>')
@api.doc(params={'site':"Site name without http prefix Ex:ndtv.com"})
class ArticlesList(Resource):
	def get(self,site):
		paper=newspaper.build("http://"+site,memoize_articles=False)
		articles={}
		i=0
		for article in paper.articles:
			articles[i]={}
			articles[i]['url']=article.url
<<<<<<< HEAD
=======
			# article.download()
			# article.parse()
			# article.nlp()
			# articles[i]['text']=article.text
			# articles[i]['authors']=article.authors
			# articles[i]['summary']=article.summary
			# articles[i]['keywords']=article.keywords
>>>>>>> 737b67b72255bfa03e52d3e3fbf3696aae283306
			i=i+1
		return {'size':i,'articles':articles}

resource_fields = {
	'site_url':fields.Url,
}
@api.route('/api/v1/scrape-article/<string:site_url>')
class ArticleInfo(Resource):
	def get(self,site_url):
		url=urllib.unquote(site_url)
		print site_url
		return {'message':"hello world"}

@api.route('/index')
class Home(Resource):
    def get(self):
        return {'hello': 'world'}


if __name__ == "__main__":
    app.run()
