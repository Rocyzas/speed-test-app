from flask import jsonify
import nltk
import random

if not nltk.corpus.words.words():
    nltk.download('words')

from nltk.corpus import words

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

def ManageDifficultyText(difficulty):


    prompts = {
        'easy': getEasyText(50),
        'medium': 'This is a medium text.',
        'hard': 'This is a hard text.'
    }
    
    if difficulty in prompts:
        return jsonify({'prompt': prompts[difficulty]})
    else:
        return jsonify({'error': 'Invalid difficulty level'}), 400

def getEasyText(n):
    english_words = words.words()
    easy_words = [word for word in english_words if len(word) <= 5]
    random_word_list = random.sample(easy_words, n)
    return ' '.join(random_word_list)
