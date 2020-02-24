import urllib3
import shutil
import json
import requests


json_obj = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

r = requests.get(json_obj)

jsono = r.json()



print(jsono["hdurl"])