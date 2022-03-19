import requests, os
from time import sleep
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('API_KEY')

class TemporaryGmail():
    
    def __init__(self):
        pass

    def read(sefl, email):
        url_read = f"https://temp-mail44.p.rapidapi.com/api/v3/email/{email}/messages"
        headers = {
            'x-rapidapi-host': "temp-mail44.p.rapidapi.com",
            'x-rapidapi-key': TOKEN
        }
        response = requests.request("GET", url_read, headers=headers)
        sleep(10)
        for response.json()[0]['subject'] in response.json():
            return response.json()[0]['subject']