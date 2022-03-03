import random
import string
from bs4 import BeautifulSoup
import requests
import time
   
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
   
    
    def email(self):
        r = requests.get('https://email-fake.com/')
        data = r.text
        soup = BeautifulSoup(data, "html.parser")
        print('Getting mail...')
        return soup.find("span", id="email_ch_text")

    def generator_usernames(self):
        with open("usernames.txt", "r") as f:
            content = f.readlines()
            random_number = str(random.randint(100, 999999))
            random_username = random.choice(content)
            return random_username + random_number

    def password(self):
        characters = string.ascii_letters
        account_password = '' .join(random.choice(characters) for _ in range(10))
        print(">>> Password: ",account_password)
        return account_password



    def email_confirmation_code(self, email):
        time.sleep(10)
        print("Check if email is  correct...", email.email)
        url = f'https://email-fake.com/{email.text}'
        print(f"URL: {url}")
        c = True
        while c:
            try:
                r_code = requests.get(url, headers={
                "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
                })
            except requests.exceptions.ConnectionError:
                pass
            else: 
                time.sleep(1)
                if r_code.status_code == 200:
                    print(f"{bcolors.OKGREEN}", r_code.status_code,"OK",f"{bcolors.ENDC}")
                    time.sleep(2)
                    data = r_code.text
                    time.sleep(2)
                    soup = BeautifulSoup(data, "html.parser")
                    time.sleep(1)
                    the_code = soup.find('h1')
                    code = the_code.text[:6]
                    if code.isnumeric() == True:
                        print(">>> The confirmation code:", code)
                    else:
                        print(">>> Retry...", end="\r")
                        
        return code