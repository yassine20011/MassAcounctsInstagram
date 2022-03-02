
# Author : Yassine Amjad

from os import close
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
import random
import string
import time
from selenium.webdriver.support.ui import Select
from get_email import *

options = webdriver.ChromeOptions()
ua = UserAgent()
userAgent = ua.random
print(userAgent)
options.add_argument(f'user-agent={userAgent}')
options.add_argument('user-data-dir=C:\\Users\\AMJAD\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
browser = webdriver.Chrome(executable_path=r"C:\Webdrivers\chromedriver.exe", chrome_options=options)
#browser = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Webdrivers\chromedriver.exe')
browser.get("https://www.instagram.com/accounts/emailsignup/")

time.sleep(5)


def start():
    # Generate Email & Password
    #name = '' .join(random.choice(Email) for x in range(10)) + '@gmail.com'
    characters = string.ascii_letters
    get_email = mail.Email.text
    print(f"Email use it : {get_email}")
    account_password = '' .join(random.choice(characters) for _ in range(10))
    print(">>> Password: ",account_password)
    with open("usernames.txt", "r") as f:
        content = f.readlines()
        RandomNumber = random.randint(100, 999999)
    IG_username = random.choice(content)
# Send selenium to find element by name and put generated Email in input  the specific for it.
    time.sleep(5)
    email = browser.find_element_by_name('emailOrPhone')
    with open("data.txt", "a") as log_in_info:
        log_in_info.write("\nEmail : " + get_email)
        email.send_keys(get_email)
# take a nap

        time.sleep(3)
# Send selenium to find element by name and put generated fullname in input  the specific for it.
        time.sleep(5)
        fullname = browser.find_element_by_name('fullName')
        fullname.send_keys(IG_username)
# take a nap

        time.sleep(3)
# Send selenium to find element by name and put generated username in input  the specific for it.
        time.sleep(5)
        username = browser.find_element_by_name('username')
        log_in_info.write("\nUsername : " + IG_username)
        username.send_keys(IG_username + str(RandomNumber))
# Take a nap

        time.sleep(3)
# Send selenium to find element by name and put generated password in input  the specific for it.
        password = browser.find_element_by_name('password')
        log_in_info.write(f"Password : {account_password}")
        log_in_info.write("                       \n#############################                                             ")
    password.send_keys(account_password)
# Find a the button with xpath and click it

    Register = browser.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[7]/div/button')
    Register.click()
# Take a nap

    print('>>> Start a nap in 0s..')
    time.sleep(6)
    print('>>> Wake Up')
# Enter a valid Birthday

    option_value = "2000"
    select_element = browser.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select')
    select = Select(select_element)
    select.select_by_value(option_value)
# Take a nap

    time.sleep(5)
# This to Click at button next

    Click_button = browser.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/div/div[1]/div/div[6]/button')
    Click_button.click()
# sending code..
    from email_sms import sms


    key1 = sms().key
    time.sleep(6)
    code_of_confirmation = browser.find_element_by_name('email_confirmation_code')
    code_of_confirmation.send_keys(key1)
# This to Click at button next


    time.sleep(3)
    Click_button = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div/div[2]/button')
    Click_button.click()
# Message from instagram Activer les notifications

    #time.sleep(3)
    #plus_tard = browser.find_element_by_xpath('/html/body/div[5]/div/div/#div/div[3]/button[1]]')
    #plus_tard.click()
# follow me 

    from email_sms import bcolors

    print(f"{bcolors.OKGREEN}",">>> Task successfuly Passed :)",f"    {bcolors.ENDC}")

start()


exit()