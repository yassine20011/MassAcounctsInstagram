import requests
import time
from bs4 import BeautifulSoup
from get_email import mail
from fake_useragent import UserAgent

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



class sms:
    time.sleep(10)
    ua = UserAgent()
    userAgent = ua.random
    #print(userAgent)
    url = f'https://email-fake.com/{mail.Email.text}'
    print(f">> URL: {url}")
    c = True
    while c:
        try:
            r_code = requests.get(url, headers={
            "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
            })
        except requests.exceptions.ConnectionError:
            pass
        else: 
            r_code
            time.sleep(0.9)
            if r_code.status_code == 200:
                print(f"{bcolors.OKGREEN}", r_code.status_code,"OK",f"{bcolors.ENDC}")
                time.sleep(2)
                data2 = r_code.text
                time.sleep(2)
                soup_2 = BeautifulSoup(data2, "html.parser")
                time.sleep(1)
                the_code = soup_2.find('h1')
                key = the_code.text[:6]
                print(">>> The confirmation code:", key)
                c = key.isnumeric() == False