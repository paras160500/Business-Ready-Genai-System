from IPython.display import display, HTML

import re



# Step 1: Load and Display Conversation Log

def load_and_display_conversation_log():

    try:

        with open("conversation_log.txt", "r") as log_file:

            conversation_log = log_file.readlines()

        

        # Prepare HTML for display

        html_content = "<h3>Loaded Conversation Log</h3><table border='1'>"

        for line in conversation_log:

            html_content += f"<tr><td>{line.strip()}</td></tr>"

        html_content += "</table>"



        # Display the HTML

        display(HTML(html_content))

        

        return conversation_log

    except FileNotFoundError:

        print("Error: conversation_log.txt not found. Ensure it exists in the current directory.")

        return []



# Step 2: Clean the conversation log by removing punctuations and special characters

def cleanse_conversation_log(conversation_log):

    cleansed_log = []

    for line in conversation_log:

        # Remove problematic punctuations and special characters

        cleansed_line = re.sub(r"[^\w\s,.?!:]", "", line)

        cleansed_log.append(cleansed_line.strip())

    return " ".join(cleansed_log)  # Combine all lines into a single string



# Step 3: Initialize `uinput` with the cleansed conversation log to continue the conversation

def initialize_uinput(cleansed_log):

    if cleansed_log:

        print("\nCleansed conversation log for continuation:")

        print(cleansed_log)

        return cleansed_log  # Use the cleansed log as the new input

    else:

        print("Error: No data available to initialize `uinput`.")

        return ""