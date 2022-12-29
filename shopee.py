from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time

user_name = 'wanchuenshin'
password = 'Bbh19971992'

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.set_window_size(720, 720)
url ='https://shopee.tw/'
driver.get(url)

time.sleep(3)

# input('input any key')

tmp = driver.find_element(By.XPATH, '//a[contains(@class, "login")]')
login_url = tmp.get_attribute("href")

driver.get(login_url)

# input('input any key')
time.sleep(3)

driver.find_element(By.XPATH, '//input[contains(@placeholder, "Email")]').send_keys(user_name)
time.sleep(0.5)
driver.find_element(By.XPATH, '//input[contains(@placeholder, "密碼")]').send_keys(password)
time.sleep(0.5)
driver.find_element(By.XPATH, '//button[contains(text(), "登入")]').click()

# input('input any key')
time.sleep(1)

driver.get('https://shopee.tw/shopee-coins')

# input('input any key')
time.sleep(1.5)

driver.find_element(By.XPATH, '//button[contains(text(), "蝦幣")]').click()


input('input any key')
print('end')