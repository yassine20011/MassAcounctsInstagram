
"""
import requests
import time 
from bs4 import BeautifulSoup
from Email import mail
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


class sms():
    ua = UserAgent()
    userAgent = ua.random
    print(userAgent)
    time.sleep(5)
    url = 'https://email-fake.com/' + mail.Email.text
    print(">> URL: " + url)
    c = True
    while c:
        r_code = requests.get(url, f'user-agent{userAgent}')
        time.sleep(2)
        print(r_code.status_code)
        if r_code.status_code == 200:
            c = False
            time.sleep(2)
            data2 = r_code.text
            time.sleep(2)
            soup_2 = BeautifulSoup(data2, "html.parser")
            time.sleep(1)
            the_code = soup_2.find('h1')
            key = the_code.text[0:6]
            print(">>> The confirmation code:", key)
            print(f"{bcolors.OKGREEN}", r_code.status_code,"OK",f"{bcolors.ENDC}")


"""

c = True == False

print(c)