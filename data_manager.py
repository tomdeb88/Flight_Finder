import os
import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT="https://api.sheety.co/96fd27c8901e7407d06fb5078cdc3e3d/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.username=os.environ.get('SHEETY_USERNAME')
        self.password=os.environ.get('SHEETY_PASSWD')
        self.authorization=HTTPBasicAuth(username=self.username,password=self.password)
        self.cities_data={}
        self.get_cities_data()


    def get_cities_data(self):
        response=requests.get(url=SHEETY_ENDPOINT,auth=self.authorization)
        data=response.json()
        self.cities_data=data['prices']
        return self.cities_data
