import re 
from openai_api import make_openai_api_call

def cleanse_conversational_log(message_obj):
    """
        Convert the conversational message into a normal string
    """

    conversational_str = " ".join(
        [f"{entry['role']} : {entry['content']}" for entry in message_obj]
    )

    # Removing the problamatic Punctuations
    return re.sub(r"[^\w\s,.?!:]", "", conversational_str)

def conversational_agent(initial_user_input,mrole,mcontent,user_role,user_name):
    
    # Setting up messages_obj to append the rest messages to it.
    messages_obj = [
        {'role' : mrole , 'content' : mcontent}
    ]

    # Greetings to user
    print("Welcome to the conversational Agent; Press q to quit and end conversation")

    # Handle User Input
    if initial_user_input:
        print(f"{user_name} : {initial_user_input}")
        messages_obj.append({'role' : user_role , 'content' : initial_user_input})

        # Cleaning the message_obj for printing logging and so on...make it easy string
        conversation_string = cleanse_conversational_log(messages_obj)

        # Make an API Call with cleansing obj
        try:
            agent_response = make_openai_api_call(
                input= conversation_string,
                mrole = mrole,
                mcontent = mcontent,
                user_role = user_role 
            )
        except Exception as e:
            print(f"Error calling the API call in the conversational_agent : {str(e)}")
            agent_response = 'Sorry, I encounterd an error while calling the API.'

        # Save the assistant response to the messages_obj
        messages_obj.append(
            {'role' : 'assistant' , 'content' : agent_response}
        )

        print(f"Agent : {agent_response}")

    while True:
        # Take user input
        user_input = input(f"{user_name} : ")

        # Checking the quit condition
        if user_input.lower() in ['quit' , 'q']:
            print("Exit the conversation")
            break

        # Append the user message to the main messages_obj
        messages_obj.append(
            {'role' : user_role , 'content' : user_input}
        )

        # Cleansing the messages_obj
        conversation_string = cleanse_conversational_log(messages_obj)

        # Call the API
        try:
            agent_response = make_openai_api_call(
                input = conversation_string,
                mrole = mrole,
                mcontent=mcontent,
                user_role=user_role
            )
        except Exception as e:
            print(f"error during calling the API this time in the while loop")
            agent_response = "Sorry, I encountered an error processing your input."

        # Appending to the messages_obj
        messages_obj.append({'role' : 'assistant' , 'content' : agent_response})

        # Display the assistant response 
        print(f"Agent : {agent_response}")


    # Save conversation to log file 
    with open("conversation_log.txt" , "w") as file:
        file.write(
            '\n'.join([f"{(user_name if entry['role'] == 'user' else entry['role'])} : {entry['content']}" for entry in messages_obj])
        )

    # Final Print
    print("Conversation saved to 'conversation_log.txt'.")


def run_conversational_agent(uinput,mrole,mcontent,user_role,user_name):
    conversational_agent(uinput,mrole,mcontent,user_role,user_name)