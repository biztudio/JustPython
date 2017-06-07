from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Python RESTful'

@app.route('/articles', methods=['GET'])
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>', methods=['GET'])
def api_article(articleid):
    return 'You are reading ' + articleid

if __name__ == '__main__':
    app.run(debug=True)
