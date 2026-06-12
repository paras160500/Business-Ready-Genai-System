import openai 
import os 
from dotenv import load_dotenv

load_dotenv()

def initializa_pinecone_api():
    PINECONE_API_KEY = os.getenv("pinecone_api")

    if not PINECONE_API_KEY:
        print("CAnt find PineCone API in the pinecone_Setup.py")
        raise ValueError("Cant find the pinecone api")
    
    os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
    print("PINECONE_API_KEY initialized successfully.")