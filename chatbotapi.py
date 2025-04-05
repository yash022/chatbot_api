from flask import Flask, jsonify 
import os
import requests
api_key = os.environ.get("API_KEY")
API_URL = "https://api.together.xyz/v1/chat/completions"

def chat_with_gpt(prompt):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",  # You can change the model here
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        reply = response.json()["choices"][0]["message"]["content"].strip()
        return reply
    except Exception as e:
        return f"Error: {e}"
    
app = Flask(__name__) 
@app.route('/') 
def hello_world(): 
    return 'Hello, World!' 

@app.route('/reply/<string:query>')
def reply(query):
    if query.lower() in ["quit", "exit", "bye"]:
            return "bye"
    else:
        response = chat_with_gpt(query)
        return response
    
if __name__ == "__main__":
    app.run(debug=True)
