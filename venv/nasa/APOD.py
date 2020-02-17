import urllib3
import shutil

global path


def nasa_image():
    ## Url for the nasa web service to get the today image from space
    url = "https://apod.nasa.gov/apod/image/2002/Eta-HST-ESO-New-LL.jpg"

    c = urllib3.PoolManager()

    # get the image from the url and save it into the test.png file
    with c.request('GET', url, preload_content=False) as resp, open("test.png", 'wb') as out_file:
        shutil.copyfileobj(resp, out_file)



    resp.release_conn()

def get_img_path():
    path = "test.png"
    return path

nasa_image()

print(get_img_path())