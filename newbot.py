from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

username = ('YourInstagramUsername')
password = ('YourInstagramPassword')

chromedriver_path = '/Your/chromedriver/path' # Change this to your own chromedriver path! Also please check your webdrive version
webdriver = webdriver.Chrome()
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)
username = webdriver.find_element_by_name('username')
username.send_keys('YourInstagramUsername')
password = webdriver.find_element_by_name('password')
password.send_keys('YourInstagramPassword')
submit = webdriver.find_element_by_tag_name('form')
submit.submit()
