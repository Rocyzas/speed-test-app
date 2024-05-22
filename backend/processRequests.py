from flask import jsonify

def ProcessUserInput(userInput):
    try:
        counter = len(userInput.split())
        return jsonify({'user_input': userInput + ' - ' + str(counter)}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred'}), 500