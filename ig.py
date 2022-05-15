# Author : Yassine Amjad
# Version : 1.0.0
# Description : This is a simple script to register on instagram
# Usage : python3 ig.py
# Notes :
#   - This script is not optimized for speed
#   - This script is not optimized for security
#   - This script is not optimized for performance
#   - This script is not optimized for stability
# Requirements :
#   - Python 3.6.x
#   - Selenium
#   - Chrome
#   - Webdriver
#   - Dotenv
#   - Requests
#   - BeautifulSoup
#   - Random
#   - time
#   - os
# Status :
#   - Working
#   - Tested on Windows 11 and Windows 10

from components import bcolors
print(f"{bcolors.OKGREEN}",">>> Instagram Register",f"{bcolors.ENDC}")
print(f"{bcolors.OKGREEN}",">>> By Yassine Amjad",f"{bcolors.ENDC}")


print(" __  __                                                    _         _           _                                  ")
print("|  \/  |                                                  | |       | |         | |                                 ")
print("|  |\/| | __ _ _ __   __ _ _ __ ___   __ _ _ __   __ _  __| |_   _  | |__   __ _| |_ ___  _ __ ___   ___ _ __ ___ ")
print("|  |  | |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ / _` |/ _` | | | | | '_ \ / _` | __/ _ \| '_ ` _ \ / _ \ '__/ __|")
print("|  |  | | (_| | |_) | (_| | | | | | | (_| | | | | (_| | (_| | |_| | | | | | (_| | ||  __/| | | | | |  __/ |  \__ \")")



from selenium import webdriver
from fake_useragent import UserAgent
import time, random
from selenium.webdriver.support.ui import Select
from components import Components
from temp_mail import TemporaryGmail
from selenium.webdriver.common.by import By


ua = UserAgent()
userAgent = ua.random
options = webdriver.ChromeOptions()
options.add_argument("--log-level=OFF")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument(f'user-agent={userAgent}')
options.add_argument('user-data-dir=C:\\Users\\AMJAD\\AppData\\Local\\Google\\Chrome\\User Data\\Default')

browser = webdriver.Chrome(executable_path=r"C:\Webdrivers\chromedriver.exe", chrome_options=options)


print("Stating...\n")

browser.delete_all_cookies()
browser.get("https://instagram.com/accounts/emailsignup/")
components = Components()
email = components.get_email()
username = components.generator_usernames()
password = components.password()


def login_form():
	" This function is to fill the login form "

	time.sleep(1)
	find_element_email = browser.find_element(By.NAME ,'emailOrPhone')
	find_element_email.send_keys(email["email"])

	with open("data.txt", "a") as log_in_info:
		log_in_info.write("\nEmail : " + email["email"])

		time.sleep(2)
		fullname = browser.find_element(By.NAME ,'fullName')
		fullname.send_keys(username)

		time.sleep(2)
		find_element_username = browser.find_element(By.NAME ,'username')
		log_in_info.write("\nUsername : " + username)
		find_element_username.send_keys(username)
		time.sleep(2)
		find_element_password = browser.find_element(By.NAME ,'password')
		log_in_info.write(f"Password : {password}")
		log_in_info.write("\n#############################")
		find_element_password.send_keys(password)

		time.sleep(5)

		Register = browser.find_element(By.XPATH,"/html/body/div[1]/section/main/div/div/div[1]/div/form/div[7]/div/button")
		Register.click()



def birthday_form():
	" This function is to fill the birthday form "

	time.sleep(2)
	option_value = str(random.randint(1975, 2001))
	select_element = browser.find_element(By.XPATH,
	'//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select')
	select = Select(select_element)
	select.select_by_value(option_value)
	time.sleep(2)

	Click_button = browser.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/div/div[1]/div/div[6]/button')
	Click_button.click()

def confirmation():
	" This function is to confirm the registration "
	
	temporary_gmail = TemporaryGmail()
	count = 1
	while True:
		print(f"Waiting for confirmation code... Number of tries {count}", end="\r")
		if temporary_gmail.read(email["email"]) is not None:
			code = temporary_gmail.read(email["email"])[:6]
			print("\nConfiramation code: ", code)
			time.sleep(2)
			code_of_confirmation = browser.find_element(By.NAME ,'email_confirmation_code')
			code_of_confirmation.send_keys(code)
			break
		count += 1
		continue

	time.sleep(2)
	Click_button = browser.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div/div[2]/button')
	Click_button.click()
	from components import bcolors
	print(f"{bcolors.OKGREEN}",">>> Task successfuly Passed :)",f"{bcolors.ENDC}")


def start():
	" This is the main function "

	# Register
	login_form()
	birthday_form()
	confirmation()
	for i in range(-60, 1):
		print(f"Browser will be closed in {i * - 1} seconds", end='\r')
		time.sleep(1)
	browser.close()
	
	# Create mass accounts not recommended

	"""
	while True:
		login_form()
		birthday_form()
		confirmation()
		for i in range(-60, 1):
			print(f"Browser will be closed in {i * - 1} seconds", end='\r')
			time.sleep(1)
			browser.close()
	"""


start()
