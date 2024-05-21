from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/difficulty/<difficulty>', methods=['GET'])
def get_prompt(difficulty):
  prompt = f"This is a sample prompt for {difficulty} difficulty."
  return jsonify({'prompt': prompt})

@app.route('/', methods=['GET'])
def get_home():
    return "HOME"

if __name__ == '__main__':
  app.run(debug=True)
