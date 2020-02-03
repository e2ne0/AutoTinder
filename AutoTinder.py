from selenium import webdriver
from time import sleep

class TinderBot():
	def __init__(self):
		self.driver = webdriver.Firefox()
		self.driver.get('https://tinder.com/?lang=zh-Hant')

	def login(self):
		fb_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/div[2]/button')
		fb_btn.click()
		sleep(2)
		base_window = self.driver.window_handles[0]
		self.driver.switch_to_window(self.driver.window_handles[1])

		email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
		email_in.send_keys('myemail')

		pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
		pw_in.send_keys('password')

		login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
		login_btn.click()