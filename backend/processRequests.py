from flask import jsonify

def ProcessUserInput(userInput):
    try:
        counter = len(userInput.split())
        return jsonify({'user_input': userInput + ' - ' + str(counter)}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred'}), 500

def ManageDifficultyText(difficulty):
    prompts = {
        'easy': 'This is an easy prompt.',
        'medium': 'This is a medium prompt.',
        'hard': 'This is a hard prompt.'
    }
    
    if difficulty in prompts:
        return jsonify({'prompt': prompts[difficulty]})
    else:
        return jsonify({'error': 'Invalid difficulty level'}), 400
