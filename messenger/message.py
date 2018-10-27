from selenium import webdriver
from time import sleep

USERNAME = "snzahedian@gmail.com" # your Facebook username
PASSWORD = "" # your Facebook password
MESSAGE = "" # message to send 
RECIPIENTS = ["Saam Zahedian"] # list of strings of message recipients
PATH = '/Users/SaamZahedian/Documents/Academic_Fun/fun_useful/messenger/chromedriver' # path to ChromeDriver executable


def merge_message(user_name, pass_word, message, recipients, path):
	options = webdriver.chrome.options.Options()
	options.add_argument("--disable-notifications")
	browser = webdriver.Chrome(executable_path=path, options=options)
	browser.get('https://www.facebook.com/')

	# open page and login
	username = browser.find_element_by_name('email')
	username.send_keys(user_name)
	password = browser.find_element_by_name('pass')
	password.send_keys(pass_word)
	login = browser.find_element_by_id('loginbutton')
	login.click()

	# open Messenger
	messenger_link = browser.find_element_by_id('navItem_217974574879787')
	messenger_link.click()

	sleep(3)

	for recipient in recipients:
		# start conversation 
		new_message = browser.find_element_by_xpath("//a[@aria-label='New Message']")
		new_message.click()

		sleep(2)

		# enter recipient
		name = browser.find_element_by_xpath("//input[@placeholder='Type the name of a person or group']")
		name.send_keys(recipient)

		sleep(2)

		# hit enter
		action = webdriver.common.action_chains.ActionChains(browser)
		action.send_keys(u'\ue007')
		action.perform()

		sleep(2)

		# click on message bar and type message
		message_bar = browser.find_element_by_xpath("//div[@aria-label='Type a message...']")
		message_bar.click()
		message_bar.send_keys(message)

		action.send_keys(u'\ue007')
		action.perform()

		sleep(2)


merge_message(USERNAME, PASSWORD, MESSAGE, RECIPIENTS, PATH)
