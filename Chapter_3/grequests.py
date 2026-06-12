import os
from urllib.request import urlretrieve

def download(directory, filename):
    # Use the raw file URL instead of the HTML page
    base_url = "https://raw.githubusercontent.com/Denis2054/Building-Business-Ready-Generative-AI-Systems/main/"
    file_url = f"{base_url}{directory}/{filename}"

    save_dir = "Download"
    os.makedirs(save_dir, exist_ok=True)

    save_path = os.path.join(save_dir, filename)

    try:
        urlretrieve(file_url, save_path)
        print(f"Downloaded {filename} to {save_path}")
    except Exception as e:
        print("Error in grequest.py")
        print(str(e))
