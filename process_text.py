import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def process_text_with_groq(text):
    api_key = os.getenv('GROQ_API_KEY')
    url = 'https://api.groq.com/openai/v1/chat/completions'

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    payload = {
        'model': 'llama3-groq-70b-8192-tool-use-preview',
        'messages': [
            {'role': 'user', 'content': f"You are an assistant designed to organise course materials into structured notes. "
        "Given the input text, extract key points and group related content under clear headings and subheadings, "
        "and summarise where necessary to make the notes concise and informative. "
        "Make sure all the important information is included in the notes. The content: "
        f"\n{text}"}
        ],
        'temperature': 0.3,
        'max_tokens': 5000
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return ""
