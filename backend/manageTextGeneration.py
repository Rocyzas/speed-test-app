import os
import openai

from flask import jsonify


openai.api_key = os.getenv('OPENAI_API_KEY')

def callChatGPT(difficulty):
    try:
        # Send request to OpenAI API for completion
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Generate " + difficulty + " text containing exactly 10 words."}
            ]
        )
        
        generated_text = completion.choices[0].message.content
        
        return generated_text
    except Exception as e:
        print('---> Error:', e)
        return jsonify({"error": "An error occurred", "details": str(e)}), 500
    
def GenerateText(difficulty):
    prompts = ['easy', 'medium', 'hard']

    if difficulty in prompts:
        return jsonify({'prompt': callChatGPT(difficulty)})
    else:
        return jsonify({'error': 'Invalid difficulty level'}), 400
