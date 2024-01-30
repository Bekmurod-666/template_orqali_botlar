import logging

import requests

url = "https://background-removal.p.rapidapi.com/remove"

payload = {"image_url": "https://objectcut.com/assets/img/raven.jpg"}
headers = {
    "content-type": "application/x-www-form-urlencoded",
    "X-RapidAPI-Key": "f33196b31amsh2f71ffa4d57ee7dp1bbdd1jsnd54d0c27205e",
    "X-RapidAPI-Host": "background-removal.p.rapidapi.com"
}

# response = requests.post(url, data=payload, headers=headers)
#
# print(response.json())

async def remove_background(img_url):
    payload = f"image_url = {img_url}"
    response = requests.request('POST',url,data=payload,headers=headers)
    # logging.info(response.json()['response']['image_url'])
    return response.json()['response']['image_url']