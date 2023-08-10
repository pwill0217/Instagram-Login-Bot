from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

username = ('gooodwillll')
password = ('lolsir217')

chromedriver_path = '/usr/local/bin/chromedriver 2' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome()
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)
username = webdriver.find_element_by_name('username')
username.send_keys('gooodwillll')
password = webdriver.find_element_by_name('password')
password.send_keys('lolsir217')
submit = webdriver.find_element_by_tag_name('form')
submit.submit()