from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
Username = os.environ.get('your username')
Password = os.environ.get('your password')

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

url = "https://www.taneps.go.tz/cas/login?service=https%3A%2F%2Fwww.taneps.go.tz%2Fepps%2Fauthenticate%2Flogin%3Fcallback%3Dtrue"
path = "C:\Development\chromedriver.chromedriver.exe"

service = Service(executable_path=path)

driver = webdriver.Chrome(options=chrome_options, service=service)
driver.get(url)

time.sleep(3)

username_input = driver.find_element(by=By.ID, value="Username")
username_input.send_keys("your username")

password_input = driver.find_element(by=By.ID, value="Password")
password_input.send_keys("Your password")

password_input.send_keys(Keys.ENTER)
