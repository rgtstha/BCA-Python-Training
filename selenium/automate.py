from selenium import webdriver
from  selenium.webdriver.common.by import By
import time

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')

driver = webdriver.Chrome()
driver.get('http://the-internet.herokuapp.com/login')

username_element = driver.find_element(By.NAME, 'username')
username_element.send_keys('tomsmith')

password_element = driver.find_element(By.NAME, 'password')
password_element.send_keys('SuperSecretPassword!')

login_button = driver.find_element(By.TAG_NAME, 'button')
login_button.click()
time.sleep(5)

subheader_element = driver.find_element(By.CLASS_NAME, 'subheader')
subheader_element.text
driver.close()