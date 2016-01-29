from flask import Flask
from flask_restplus import Resource, Api, fields, marshal_with
import newspaper,json
from newspaper import Article
import nltk
app = Flask(__name__)
api = Api(app)

@api.route('/api/v1/get-articles/<string:site>')
@api.doc(params={'site':"Site name without http prefix Ex:ndtv.com"})
class ArticleList(Resource):
	def get(self,site):
		print site
		paper=newspaper.build("http://"+site)
		articles={}
		i=0
		for article in paper.articles:
			articles[i]={}
			articles[i]['url']=article.url
			i=i+1
		return {'size':i,'articles':articles}

@api.route('/api/v1/scrape-article/<path:url>/<string:name>/<string:profession>')
class ArticleInfo(Resource):
	def get(self,url,name,profession):
		article = Article(url)
		article.download()
		article.parse()
		article.nlp()
		article_data = {}
		article_data['url']=url
		article_data['title']=article.title
		article_data['keywords']=article.keywords
		article_data['summary']=article.summary
		article_data['text']=article.text
		article_data['top_image']=article.top_image
		article_data['publish_date']=str(article.publish_date)
		article_data['authors']=article.authors
		article_data['movies']=article.movies
		article_data['html']=article.html
		###################################
		###### ToDo: NLP checks goes here
		for sent in nltk.sent_tokenize(article.text):
			for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
				if hasattr(chunk, 'node'):
					if chunk.node=="PERSON":
						print chunk.node, ' '.join(c[0] for c in chunk.leaves())
		nameHit=False
		profHit=False
		firstNameHit=False
		lastNameHit=False
		nameList=name.split()
		for x in article.text.split():
			if x.lower()==nameList[0].lower():
				firstNameHit=True
			if x.lower()==nameList[1].lower():
				lastNameHit=True
			if x.lower()==profession.lower():
				profHit=True
		if firstNameHit==True and lastNameHit==True:
			nameHit=True
		return {'article':article_data,'name_hit':nameHit,'profession_hit':profHit}
@api.route('/index')
class Home(Resource):
    def get(self):
        return {'hello': 'world'}


if __name__ == "__main__":
    app.run(debug=True)
