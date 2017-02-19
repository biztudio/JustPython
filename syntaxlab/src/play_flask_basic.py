from flask import Flask
app = Flask(__name__)
# An instance of the class Flask is a WSGI (Web Server Gateway Interface) application
# the argument __name__ is the name of the application's module or package


@app.route('/')
def hello_flask():
    return 'Hello, Flask!'

