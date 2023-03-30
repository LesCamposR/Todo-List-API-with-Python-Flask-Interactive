from flask import Flask, jsonify, request
app = Flask(__name__)
import json
decoded_object = json.loads(original_string)

todos = [ { "label": "My first task", "done": False } ]

@app.route('/blabla', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/todos', methods=['GET'])
def todo_get():
    json_text = jsonify(todos)
    return json_text

# suppose you have your data in the variable some_data
some_data = { "name": "Bobby", "lastname": "Rixer" }

@app.route('/one', methods=['GET'])
def one():
    # you can convert that variable into a json string like this
    json_text = jsonify(some_data)

    # and then you can return it to the front end in the response body like this
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(todos)
    print("Incoming request with the following body", request_body)
    json_text = jsonify(todos)
    return json_text


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
 app.run(host='0.0.0.0', port=3245, debug=True)