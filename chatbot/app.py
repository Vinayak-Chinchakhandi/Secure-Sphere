from flask import Flask, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address  # Correct import

load_dotenv()

app = Flask(__name__)
CORS(app)

if "Limiter" in locals(): # Only initialize limiter if the import was successful
    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=["20 per minute"]
    )

# ... rest of your app.py code ...

genai.configure(api_key=os.getenv("GOOGLE API KEY"))

model = genai.GenerativeModel('gemini-1.5-pro-latest')

@app.route('/cyber_assist', methods=['POST'])
# @limiter.limit("5 per minute") # Uncomment if you want rate limiting on this route
def cyber_assist():
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'Invalid request'}), 400
        message = data['message']

        prompt = f"""
        You are a cybersecurity expert. Provide assistance only on cybersecurity-related topics, including:
        - Phishing
        - Malware
        - Data breaches
        - Network security
        - Vulnerability analysis
        - Incident response
        - Threat intelligence
        - Security best practices

        If a user asks about a topic outside of cybersecurity, respond with:
        "This query is not related to cybersecurity. I am here to assist with cybersecurity-related aspects only, and cannot help you with that."

        Answer the following question within 75 words.

        User's question: {message}

        Your response:
        """

        response = model.generate_content(prompt)
        return jsonify({'result': response.text})
    except Exception as e:
        print(f"--- API Error: {e} ---")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)