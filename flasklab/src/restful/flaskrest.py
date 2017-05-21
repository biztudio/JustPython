from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
todos = {"1":"Fetch Milk Package", "2":"Shop for Journey", "3":"Create a Flask API"}

class TodoList_Resource(Resource):
    def get(self):
        return todos

class Todo_Resource(Resource):

    def get(self, todo_id):
        return {todo_id : todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoList_Resource, '/todos')
api.add_resource(Todo_Resource, '/todos/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
