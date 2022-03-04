# Author : Yassine Amjad

from selenium import webdriver
from fake_useragent import UserAgent
import time
from selenium.webdriver.support.ui import Select
from components import Components
import random
from temp_mail import TemporaryGmail

options = webdriver.ChromeOptions()

ua = UserAgent()
userAgent = ua.random
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument(f'user-agent={userAgent}')
options.add_argument('user-data-dir=C:\\Users\\AMJAD\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
browser = webdriver.Chrome(executable_path=r"C:\Webdrivers\chromedriver.exe", chrome_options=options)

print("Stating...\n")

browser.delete_all_cookies()
browser.get("https://instagram.com/accounts/emailsignup/")
components = Components()
items = components.get_email()
username = components.generator_usernames()
password = components.password()



def login_form():


	time.sleep(1)
	find_element_email = browser.find_element_by_name('emailOrPhone')
	find_element_email.send_keys(items["email"])

	with open("data.txt", "a") as log_in_info:
		log_in_info.write("\nEmail : " + items["email"])



		time.sleep(2)
		fullname = browser.find_element_by_name('fullName')
		fullname.send_keys(username)

		time.sleep(2)
		find_element_username = browser.find_element_by_name('username')
		log_in_info.write("\nUsername : " + username)
		find_element_username.send_keys(username)
		time.sleep(2)
		find_element_password = browser.find_element_by_name('password')
		log_in_info.write(f"Password : {password}")
		log_in_info.write("\n#############################")
		find_element_password.send_keys(password)

		time.sleep(5)

		Register = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[7]/div/button")
		Register.click()



def Birthday_form():

	time.sleep(2)
	option_value = str(random.randint(1975, 2001))
	select_element = browser.find_element_by_xpath(
	'//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select')
	select = Select(select_element)
	select.select_by_value(option_value)
	time.sleep(2)

	Click_button = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[6]/button')
	Click_button.click()
	




def confirmation():
	# sending code..
	temporary_gmail = TemporaryGmail()
	while True:
		if temporary_gmail.read(items["email"]) is not None:
			code = temporary_gmail.read(items["email"])[:6]
			print(code)
			time.sleep(2)
			code_of_confirmation = browser.find_element_by_name('email_confirmation_code')
			code_of_confirmation.send_keys(code)
			break
		continue

	time.sleep(2)
	Click_button = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div/div[2]/button')
	Click_button.click()
	from components import bcolors
	print(f"{bcolors.OKGREEN}",">>> Task successfuly Passed :)",f"{bcolors.ENDC}")



def start():
	login_form()
	Birthday_form()
	confirmation()
start()