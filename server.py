from flask import Flask,render_template
import newspaper,json
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/api/v1/scrape-articles/<site>')
def apiScrapeArticles(site=None):
	print site
	paper=newspaper.build("http://"+site+".com")
	for article in paper.articles:
		print article.url
	return "hello"

if __name__ == "__main__":
    app.run()