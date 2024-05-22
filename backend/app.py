from flask import Flask, request, jsonify
from flask_cors import CORS

from processRequests import ProcessUserInput

app = Flask(__name__)
CORS(app)

@app.route('/api/difficulty/<difficulty>', methods=['GET'])
def get_difficulty(difficulty):
  prompt = "This is a sample prompt for {} difficulty.".format(difficulty)
  return jsonify({'prompt': prompt})


@app.route('/api/userInput', methods=['POST'])
def get_user_input():
    return ProcessUserInput(request.json.get('input'))

@app.route('/', methods=['GET'])
def get_home():
    return "HOME"

if __name__ == '__main__':
  app.run(debug=True)
