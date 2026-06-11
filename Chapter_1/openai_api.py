import openai
from openai import OpenAI
import base64
import os 
from dotenv import load_dotenv
load_dotenv()


openai_api_key = os.getenv("open_ai_api")
client = OpenAI(api_key=openai_api_key)

def make_openai_api_call(input , mrole , mcontent , user_role):
    gmodel = "gpt-4o"

    # Creating message Obj
    messages_obj = [
        {
            'role' : mrole,
            'content' : mcontent
        },
        {
            'role' : user_role,
            'content' : input
        }
    ]

    params = {
        "temperature": 0,
        "max_tokens": 1024,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }

    client = OpenAI(api_key=openai_api_key)

    response = client.chat.completions.create(
        model = gmodel,
        messages= messages_obj,
        **params
    )

    return response.choices[0].message.content




