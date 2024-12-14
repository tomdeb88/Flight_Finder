import requests
import os
from dotenv import load_dotenv

load_dotenv()


AMADEUS_API_KEY=os.environ.get('AMADEUS_API_KEY')
AMADEUS_API_SECRET=os.environ.get('AMADEUS_API_SECRET')
AMADEUS_TOKEN_URL='https://test.api.amadeus.com/v1/security/oauth2/token'

token_body={
    'client_id':AMADEUS_API_KEY,
    'client_secret':AMADEUS_API_SECRET,
    'grant_type':'client_credentials'
}

response=requests.post(url=AMADEUS_TOKEN_URL,data=token_body)
access_token=response.json()['access_token']


