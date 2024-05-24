from flask import jsonify

def ProcessUserInput(userInput, prompt):
    try:
        counter = len(userInput.split())
        is_match = (userInput.strip() == prompt.strip())

        if is_match:
            print('STRINGS ARE THE SAME')

        return jsonify({
            'user_input': userInput + ' - ' + str(counter),
            'prompt': prompt,
            'match': is_match
        }), 200
    
    except Exception as e:
        return jsonify({'error': 'An error occurred',}), 500

def ManageDifficultyText(difficulty):
    prompts = {
        'easy': 'This is an easy text.',
        'medium': 'This is a medium text.',
        'hard': 'This is a hard text.'
    }
    
    if difficulty in prompts:
        return jsonify({'prompt': prompts[difficulty]})
    else:
        return jsonify({'error': 'Invalid difficulty level'}), 400
