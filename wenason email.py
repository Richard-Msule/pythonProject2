from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
username = os.environ.get('your username')
password = os.environ.get('your password')

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

url = "https://www.wenason.co.tz:2096/"
path = "C:\Development\chromedriver.chromedriver.exe"

service = Service(executable_path=path)

driver = webdriver.Chrome(options=chrome_options, service=service)
driver.get(url)

time.sleep(3)

username_input = driver.find_element(by=By.ID, value="user")
username_input.send_keys("your email")

password_input = driver.find_element(by=By.ID, value="pass")
password_input.send_keys("your password")

password_input.send_keys(Keys.ENTER)
