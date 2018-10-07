import json
import requests
import constants

#For any GET HTTP call
def get(url):
    response=requests.get(url, headers={"Authorization":"Bearer "+constants.token})
    json_data=response.json()
    return json_data
