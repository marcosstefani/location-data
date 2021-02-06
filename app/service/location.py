import json
import requests
from config.env import Env

class LocationService(object):
    def __init__(self):
        self.base_url = Env().base_url_location

    def getData(self):
        api_url = '{0}/location'.format(self.base_url)
        print("calling " + api_url)
        response = requests.get(api_url)

        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None

