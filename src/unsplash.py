import requests as _requests
import os as _os
import dotenv as _dotenv
import random as _random

_dotenv.load_dotenv()

UNSPLASH_QUERIES = ["philosophy", "life", "nature", "wisdom", "art"]
ACCESS_KEY = _os.environ["ACCESS_KEY"]

def _search_images() -> list:
    query = _random.choice(UNSPLASH_QUERIES)
    url = f"https://api.unsplash.com/search/photos?page=1&query={query}&client_id={ACCESS_KEY}"
    response = _requests.get(url)

    data = response.json()["results"]
    return data

def _get_random_image_link():
    response_data = _search_images()
    random_image_data = _random.choice(response_data)
    
    link = random_image_data["urls"]["regular"]
    return link

def download_img():
    filename = "picture.jpg"
    image_url = _get_random_image_link()
    image_response = _requests.get(image_url, stream=True)
    if image_response.status_code == 200:
        with open (filename, "wb") as image_file:
            for chunk in image_response:
                image_file.write(chunk)

download_img()