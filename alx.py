from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
user_email = os.environ.get('msuler@yahoo.com')
user_password = os.environ.get('sABINA2017')

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

url = "https://intranet.alxswe.com/"
path = "C:\Development\chromedriver.chromedriver.exe"

service = Service(executable_path=path)

driver = webdriver.Chrome(options=chrome_options, service=service)
driver.get(url)

time.sleep(3)

username_input = driver.find_element(by=By.ID, value="user_email")
username_input.send_keys("msuler@yahoo.com")

password_input = driver.find_element(by=By.ID, value="user_password")
password_input.send_keys("sABINA2017")

password_input.send_keys(Keys.ENTER)
