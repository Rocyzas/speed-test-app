from flask import jsonify

def ProcessUserInput(userInput, prompt):
    try:
        counter = len(userInput.split())
        is_match = (userInput.strip() == prompt.strip())

        prompt_words = prompt.strip().split()
        user_input_words = userInput.split()

        min_length = min(len(prompt_words), len(user_input_words))
        max_length = max(len(prompt_words), len(user_input_words))

        match_count = sum(1 for i in range(min_length) if prompt_words[i] == user_input_words[i])
        
        percent = (match_count / max_length) * 100 if min_length > 0 else 0

        return jsonify({
            'user_input': userInput,
            'prompt': prompt,
            'percent': percent
        }), 200
    
    except Exception as e:
        return jsonify({'error': 'An error occurred',}), 500
