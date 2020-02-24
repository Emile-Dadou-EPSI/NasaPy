import urllib3
import shutil
import json
import requests
global path


def nasa_image():
    ## Url for the nasa web service to get the today image from space
    urldemo = "https://api.nasa.gov/planetary/apod?api_key=O6lcyF8XnWi0w3nWQseJcvjeECQUmIRhRxyrya2R"
    urldemo2 = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=O6lcyF8XnWi0w3nWQseJcvjeECQUmIRhRxyrya2R"

    r = requests.get(urldemo)
    r2 = requests.get(urldemo2)

    json_obj2 = r2.json()
    print(json_obj2)
    url_img_mars = json_obj2["photos"][0]["img_src"]
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

def get_img_path():
    path = "test.png"
    return path

nasa_image()

print(get_img_path())