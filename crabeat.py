from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time
import getpass
from datetime import datetime
import os

'''
作者: CY
改RTK公司的密碼, 連續改240次

run python script:
activate my_sele (in RTK computer)

build exe:
pyinstaller -F -c change_password_240.py
'''


try:
    '''
    user_name = input('帳號: ')
    if user_name == '':
        print('帳號不能略過，請重新輸入')
        exit()
    base_password = input('密碼: ')
    if base_password == '':
        print('密碼不能略過，請重新輸入')
        exit()
    '''
    
    user_name = 'cychang'
    base_password = 'Deny410my957'


    print('正在啟動 chrome... 請稍後')
    access_sucess = 0
    cou = 0
    now_time = datetime.now()
    pass_word_log_file = 'pass_word_log_' + now_time.strftime("%Y%m%d_%H_%M_%S") + '.txt'

    # service = Service(executable_path='chromedriver.exe')
    # driver = webdriver.Chrome(service=service)

    options = ChromeOptions()
    driver = webdriver.Chrome(options=options)

    driver.set_window_size(1000, 800)
    url ='https://crabeats.realtek.com/Home/Login'
    driver.get(url)
    
    
    access_sucess = 0
    for a in range(20):
        try:
            driver.find_element(By.XPATH, '//input[@id="textUserId" and @placeholder="Account"]').send_keys(user_name)
            access_sucess = 1
        except:
            print('無法輸入帳號')
        if access_sucess == 1:
            break
        else:
            time.sleep(1)
    if access_sucess == 0:
        print('一直沒辦法輸入帳號')
        exit()
    
    
    access_sucess = 0
    for a in range(20):
        try:
            driver.find_element(By.XPATH, '//input[@id="textPassword" and @placeholder="Password"]').send_keys(base_password)
            access_sucess = 1
        except:
            print('無法輸入密碼')
        if access_sucess == 1:
            break
        else:
            time.sleep(1)
    if access_sucess == 0:
        print('一直沒辦法輸入密碼')
        exit()
    
    time.sleep(1)
    
    driver.find_element(By.XPATH, '//button[@type="button" and @id="buttonLogin"]').click()
    
    
    
    c = input()
    
    #driver.find_element(By.XPATH, '//input[@type="radio" and @value="瑞昱二廠"]').click()
    driver.find_element(By.XPATH, '//label[@class="k-radio-label" and @for="loc2"]').click()
    
    time.sleep(1)
    
    for i in range(10):
        now_date = driver.find_element(By.XPATH, '//input[@id="chooseMenuDate"]')
        get_date = now_date.get_attribute('value')
        print(get_date)
        if get_date == '2023/03/06':
            break
        else:
            driver.find_element(By.XPATH, '//a[@class="icon_switchDate" and @id="icon_nextDate"]').click()   # 明天
            time.sleep(1)
    
    # c = input()
    success_time = 0
    while True:
        try:
            no_menu = driver.find_element(By.XPATH, '//div[@class="alert alert-info" and @id="info_block"]')  # 找到 沒有菜單
            print('no menu')
            time.sleep(2)
            driver.find_element(By.XPATH, '//a[@class="icon_switchDate" and @id="icon_nextDate"]').click()   # 明天
            time.sleep(2)
            driver.find_element(By.XPATH, '//a[@class="icon_switchDate" and @id="icon_previousDate"]').click()   # 前一天
            time.sleep(2)
            success_time = 0
        except:
            print('可以開始訂餐嚕!')
            success_time += 1
            time.sleep(2)
            driver.find_element(By.XPATH, '//a[@class="icon_switchDate" and @id="icon_nextDate"]').click()   # 明天
            time.sleep(2)
            driver.find_element(By.XPATH, '//a[@class="icon_switchDate" and @id="icon_previousDate"]').click()   # 前一天
            time.sleep(2)
        if success_time == 3:
            break
    
    
    
    driver.close()
except Exception as e:
    print(e)
    os.system("pause")