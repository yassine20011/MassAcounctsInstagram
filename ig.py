# Author : Yassine Amjad

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import Select
from components import Components
import random

options = webdriver.ChromeOptions()

ua = UserAgent()
userAgent = ua.random
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument(f'user-agent={userAgent}')
options.add_argument('user-data-dir=C:\\Users\\AMJAD\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
browser = webdriver.Chrome(executable_path=r"C:\Webdrivers\chromedriver.exe", chrome_options=options)

time.sleep(1)

def start():
    
    print("Stating")
    browser.get("https://instagram.com/accounts/emailsignup/")
    components = Components()
    email = components.email()
    username = components.generator_usernames()
    password = components.password()
    print(f"Email: {email.text}")
# Send selenium to find element by name and put generated Email in input  the specific for it.
    time.sleep(1)
    find_element_email = browser.find_element_by_name('emailOrPhone')
    with open("data.txt", "a") as log_in_info:
        log_in_info.write("\nEmail : " + email.text)
        find_element_email.send_keys(email.text)
# Send selenium to find element by name and put generated fullname in input  the specific for it.

        time.sleep(2)
        fullname = browser.find_element_by_name('fullName')
        fullname.send_keys(username)
# Send selenium to find element by name and put generated username in input  the specific for it.
        time.sleep(2)
        find_element_username = browser.find_element_by_name('username')
        log_in_info.write("\nUsername : " + username)
        find_element_username.send_keys(username)
# Send selenium to find element by name and put generated password in input  the specific for it.
        time.sleep(2)
        find_element_password = browser.find_element_by_name('password')
        log_in_info.write(f"Password : {password}")
        log_in_info.write("\n#############################")
        find_element_password.send_keys(password)
# Find a the button with xpath and click it
    Register = browser.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[7]/div/button')
    Register.click()
# Take a nap
    time.sleep(6)
# Enter a valid Birthday
    option_value = str(random.randint(1975, 2001))
    select_element = browser.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select')
    select = Select(select_element)
    select.select_by_value(option_value)
# Take a nap
    time.sleep(2)
# This to Click at button next
    Click_button = browser.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/div/div[1]/div/div[6]/button')
    Click_button.click()
# sending code..
    code = components.email_confirmation_code(email)
    time.sleep(2)
    code_of_confirmation = browser.find_element_by_name('email_confirmation_code')
    code_of_confirmation.send_keys(code)

# This to Click at button next
    time.sleep(2)
    Click_button = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div/div[2]/button')
    Click_button.click()
    from components import bcolors
    print(f"{bcolors.OKGREEN}",">>> Task successfuly Passed :)",f"{bcolors.ENDC}")


start()