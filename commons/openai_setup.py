import openai 
import os 

def initialize_openai_api():
    API_KEY = os.getenv("open_ai_api")

    if not API_KEY:
        raise ValueError("Cant find openai api key in openai_api.py file.")
    
    os.environ['OPENAI_API_KEY'] = API_KEY
    openai.api_key = API_KEY
    print("OpenAI key Initialized successfully.")