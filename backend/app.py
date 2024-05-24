from flask import Flask, request, jsonify, session
from flask_session import Session
from flask_cors import CORS
import redis

from processRequests import ProcessUserInput, ManageDifficultyText

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_REDIS'] = redis.from_url('redis://localhost:6379')  # Adjust if Redis is on a different host or port
app.config['SESSION_COOKIE_SAMESITE'] = 'None'

# Set True only in prod
app.config['SESSION_COOKIE_SECURE'] = True  # Set to True if using HTTPS


sess = Session()
sess.init_app(app)

CORS(app, supports_credentials=True)

@app.route('/api/difficulty/<difficulty>', methods=['GET'])
def get_difficulty(difficulty):
    prompt = ManageDifficultyText(difficulty)
    session['prompt'] = prompt.get_json().get('prompt')
    # print('---> Session set with prompt:', session['prompt'])  # Debug print
    # print(session.sid)
    return prompt

@app.route('/api/userInput', methods=['POST'])
def get_user_input():
    user_input = request.json.get('input')
    # print('---> Retrieved prompt from session:', session.get('prompt'))  # Debug print
    prompt = session.get('prompt')
    # print(session.sid)
    return ProcessUserInput(user_input, prompt)

@app.route('/', methods=['GET'])
def get_home():
    return "HOME"

if __name__ == '__main__':
    app.run(debug=True)
