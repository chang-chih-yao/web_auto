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
    user_name = input('帳號: ')
    if user_name == '':
        print('帳號不能略過，請重新輸入')
        exit()
    base_password = input('密碼: ')
    if user_name == '':
        print('密碼不能略過，請重新輸入')
        exit()
    # base_password = getpass.getpass("Password: ")
    # password = 'Abcd1234_0'

    loop_num_str = input('請輸入想要改密碼的次數 (default 240): ')
    if loop_num_str == '':
        loop_num = 240      # default 240
    else:
        if loop_num_str.isdigit():
            loop_num = int(loop_num_str)
        else:
            print('please input integer')
            exit()

    print('正在啟動 chrome... 請稍後')
    access_sucess = 0
    cou = 0
    now_time = datetime.now()
    pass_word_log_file = 'pass_word_log_' + now_time.strftime("%Y%m%d_%H_%M_%S") + '.txt'

    # service = Service(executable_path='chromedriver.exe')
    # driver = webdriver.Chrome(service=service)

    options = ChromeOptions()
    driver = webdriver.Chrome(options=options)

    driver.set_window_size(720, 800)
    url ='https://damc.realtek.com/#/SignIn'
    driver.get(url)

    #time.sleep(3)
    
    access_sucess = 0
    for a in range(20):
        try:
            driver.find_element(By.XPATH, '//input[contains(@adm-input-group-input-adapter, "ctrl")]').send_keys(user_name)
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
            driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(base_password)
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

    
    access_sucess = 0
    for a in range(20):
        try:
            self_service_detect = driver.find_element(By.XPATH, '//span[contains(@ng-show, "ctrl") and contains(@adm-bind, "configurationDisplayName")]')
            if self_service_detect.text == 'Self-Service':
                access_sucess = 1
                print('找到了')
            else:
                print('還沒找到')
        except:
            print('cannot access Self-Service')
        if access_sucess == 1:
            break
        else:
            time.sleep(1)
    if access_sucess == 0:
        print('一直沒找到 Self-Service')
        exit()
        
    time.sleep(1)
    
    driver.find_element(By.XPATH, '//button[@type="submit" and @aria-label="Sign In"]').click()
    
    time.sleep(1)
        

    c = input('請先輸入完手機驗證碼後，再按任意鍵繼續...\n')
    f = open(pass_word_log_file, 'w')
    # datas = driver.find_elements(By.CLASS_NAME, 'home-card__buttons')

    for i in range(loop_num):
        click_sucess = 0
        for a in range(100):
            click_sucess = 0
            try:
                password_elements = driver.find_elements(By.XPATH, '//button[@aria-label="Change Password"]')
                for item in password_elements:
                    # print(item.text)
                    if item.text == 'CHANGE PASSWORD':
                        item.click()
                        click_sucess = 1
            except:
                #click_sucess = 0
                f.write('cannot press CHANGE PASSWORD\n')
                f.flush()
                print('cannot press CHANGE PASSWORD')
            if click_sucess == 1:
                break
            else:
                time.sleep(1)
        
            if click_sucess == 0 and a > 5:
                f.write('ERROR! 請先關閉"錯誤視窗", 再次按下"OK"後, 再按任意鍵開始')
                f.flush()
                c = input('ERROR! 請先關閉"錯誤視窗", 再次按下"OK"後, 再按任意鍵開始')

        time.sleep(1.5)
        tmp = driver.find_elements(By.XPATH, '//input[@type="password" and @adm-input-group-input-adapter="ctrl.setEditor(editor)"]')
        if len(tmp) == 3:
            cou += 1
            new_password = base_password + '_' + str(cou)
            if i == 0:
                tmp[0].send_keys(base_password)
                f.write('send_keys, base_password: '+ base_password + '\n')
                f.flush()
            else:
                tmp[0].send_keys(base_password + '_' + str(cou-1))
                f.write('send_keys, base_password + "_" + str(cou-1): '+ base_password + '_' + str(cou-1) + '\n')
                f.flush()
            time.sleep(0.5)
            tmp[1].send_keys(new_password)
            f.write('send_keys, new_password: ' + new_password + '\n')
            f.flush()
            time.sleep(0.5)
            tmp[2].send_keys(new_password)
            f.write('send_keys, new_password: ' + new_password + '\n')
            f.flush()
            time.sleep(0.5)
            print('new password:', new_password)
            f.write('new password: '+ new_password + '\n')
            f.flush()
            
            f.write('[0] get value: ' + tmp[0].get_attribute('value') + '\n')
            f.flush()
            #print('[0] get value: ' + tmp[0].get_attribute('value'))
            f.write('[1] get value: ' + tmp[1].get_attribute('value') + '\n')
            f.flush()
            #print('[1] get value: ' + tmp[1].get_attribute('value'))
            f.write('[2] get value: ' + tmp[2].get_attribute('value') + '\n')
            f.flush()
            #print('[2] get value: ' + tmp[2].get_attribute('value'))
        else:
            print('error, len(tmp) != 3')
            f.write('error, len(tmp) != 3')
            f.flush()
            break

        driver.find_element(By.XPATH, '//button[@class="wizard-nav-bar__finish md-raised flex-none md-button md-primary" and @aria-label="OK"]').click()
        f.write('press OK done\n')
        f.flush()
        print('press OK done')
        # driver.find_element(By.XPATH, '//button[@class="md-raised flex-none md-button" and @aria-label="Cancel"]').click()

        time.sleep(1)
        
        



    '''
    for a in range(10):     # try up to 10 times
        click_sucess = 0
        try:
            password_elements = driver.find_elements(By.XPATH, '//button[@aria-label="Change Password"]')
            for item in password_elements:
                # print(item.text)
                if item.text == 'CHANGE PASSWORD':
                    item.click()
                    click_sucess = 1
        except:
            click_sucess = 0
            # print('gg')
        if click_sucess == 1:
            break
        else:
            time.sleep(1)

    time.sleep(1)

    tmp = driver.find_elements(By.XPATH, '//input[@type="password" and @adm-input-group-input-adapter="ctrl.setEditor(editor)"]')
    if len(tmp) == 3:
        cou += 1
        # new_password = base_password + '_' + str(cou)
        tmp[0].send_keys(base_password + '_' + str(cou-1))
        time.sleep(0.5)
        tmp[1].send_keys(base_password)
        time.sleep(0.5)
        tmp[2].send_keys(base_password)
        time.sleep(0.5)
        print('change to original password:', base_password)
        f.write('change to original password: '+ base_password + '\n')
    else:
        print('error, len(tmp) != 3')
    driver.find_element(By.XPATH, '//button[@class="wizard-nav-bar__finish md-raised flex-none md-button md-primary" and @aria-label="OK"]').click()
    time.sleep(1)
    '''

    f.close()
    c = input('FINISHED! please input any key to continue\n')
    driver.close()
except Exception as e:
    print(e)
    os.system("pause")