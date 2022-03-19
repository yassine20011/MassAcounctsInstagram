import random, string, requests, os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('API_KEY')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Components:
    def __init__(self):
        pass
   
    def get_email(self):
        url = "https://temp-mail44.p.rapidapi.com/api/v3/email/new"
        payload = "{\r\n    \"key1\": \"value\",\r\n    \"key2\": \"value\"\r\n}"
        headers = {
            'content-type': "application/json",
            'x-rapidapi-host': "temp-mail44.p.rapidapi.com",
            'x-rapidapi-key': TOKEN
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        print(f"Email: {response.json()['email']}")
        return response.json()

    def generator_usernames(self):
        with open("usernames.txt", "r") as f:
            content = f.readlines()
            random_number = str(random.randint(100, 99999))
            random_username = random.choice(content)
            return random_username + random_number

    def password(self):
        characters = string.ascii_letters
        account_password = '' .join(random.choice(characters) for _ in range(10))
        print("Password: ", account_password)
        return account_password
