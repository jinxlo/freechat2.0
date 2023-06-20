from flask import Flask, request, jsonify, render_template
from backend.python_scripts.script import chat_with_gpt4all_model
import json

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    content = request.get_json(force=True)
    print("Request body: ", content)
    user_input = content[0]['content']
    print("User input: ", user_input)
    response = chat_with_gpt4all_model(user_input)
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
