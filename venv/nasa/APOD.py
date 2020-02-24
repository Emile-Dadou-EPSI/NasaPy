import urllib3
import shutil
import json
import requests
import random
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import date
global path


# Use a service account
cred = credentials.Certificate('/home/emile/PycharmProjects/NasaPy/venv/nasa/nasapy-35e24-firebase-adminsdk-96c4a-36d60e3eed.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


def nasa_image():
    ## Url for the nasa web service to get the today image from space
    urldemo = "https://api.nasa.gov/planetary/apod?api_key=O6lcyF8XnWi0w3nWQseJcvjeECQUmIRhRxyrya2R"
    urldemo2 = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=O6lcyF8XnWi0w3nWQseJcvjeECQUmIRhRxyrya2R"

    # Generate a random number for the picture
    num = random.randint(0, 500)

    r = requests.get(urldemo)
    r2 = requests.get(urldemo2)

    json_obj2 = r2.json()
    print(json_obj2)
    url_img_mars = json_obj2["photos"][num]["img_src"]
    print(url_img_mars)

    json_obj = r.json()
    url_img_type = json_obj["media_type"]
    url_image = json_obj["url"]
    url = url_image

    c = urllib3.PoolManager()

    if (url_img_type == 'photo'):

        # get the image from the url and save it into the test.png file
        with c.request('GET', url, preload_content=False) as resp, open("test.png", 'wb') as out_file:
            shutil.copyfileobj(resp, out_file)



        resp.release_conn()

    else :
        with c.request('GET', url_img_mars, preload_content=False) as resp, open("test2.png", 'wb') as out_file:
            shutil.copyfileobj(resp, out_file)

        resp.release_conn()

    #doc_ref = db.collections('imagesfromspace').document(u'test')
    #doc_ref.set({
     #   u'date' : date.today(),
      #  u'img_src' : "test2.png"
    #})



def get_img_path():
    path = "test.png"
    return path

nasa_image()

print(get_img_path())