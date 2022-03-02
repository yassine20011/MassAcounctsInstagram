from bs4 import BeautifulSoup
import requests
import time

class mail():
    r = requests.get('https://email-fake.com/')
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    Email = soup.find("span", id="email_ch_text")
    time.sleep(2)
    print('>>> Start')


