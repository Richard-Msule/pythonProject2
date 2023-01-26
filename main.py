from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
email = os.environ.get('msuler@yahoo.com')
password = os.environ.get('sABINA2017')

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

url = "https://www.linkedin.com/jobs/search/?currentJobId=3437920502&f_AL=true&keywords=developer&refresh=true"
path = "C:\Development\chromedriver.chromedriver.exe"

service = Service(executable_path=path)

driver = webdriver.Chrome(options=chrome_options, service=service)
driver.get(url)

time.sleep(3)
sign_in = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in.click()

username_input = driver.find_element(by=By.ID, value="username")
username_input.send_keys("msuler@yahoo.com")

password_input = driver.find_element(by=By.ID, value="password")
password_input.send_keys("sABINA2017")

password_input.send_keys(Keys.ENTER)
