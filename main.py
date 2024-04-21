import os
import sys
import time 
import daemon
import schedule
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException as ecp
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def sleep():
    time.sleep(3600)
def checkLogin():
    try:
        options = Options()
        #options.add_argument('headless')
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),options=options)
        wait = WebDriverWait(driver, 1500)
        driver.get("https://192.168.1.250/connect/PortalMain")
        loggedInText = 'Welcome to the network.'
        loggedInElement = driver.find_element(By.XPATH, f"//*[contains(text(),'{loggedInText}')]")
        print("Logged In Already")
        isLogged = True
        return True
    except ecp:
        print("Not found trying again, ecp error was raised")
        return False
    else:
        print("Different error raised")
        print(Exception)

def portalLogin(userid, password):
    try:
        options = Options()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),options=options)
        driver.get("https://192.168.1.250/connect/PortalMain")
        loginElement = WebDriverWait(driver, 2000).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#LoginUserPassword_auth_username.formInput')))
        loginElement = driver.find_element(By.CSS_SELECTOR,'#LoginUserPassword_auth_username.formInput')
        loginElement.send_keys(userid)
        loginElement = driver.find_element(By.ID,'LoginUserPassword_auth_password')
        loginElement.send_keys(password)
        loginButton = driver.find_element(By.ID,'UserCheck_Login_Button_span')
        loginButton.click()
        isLogged = True
    except ecp:
        print('login failed! Trying again')
        failedLogin+=1
def main():
    failedCheck = 0
    failedLogin = 0
    myid = 'B323049'
    mypass = 'B323049'
    check = checkLogin()
    if check == True:
        ("Already logged in!")
        sleep()
        main()
    elif check == False:
        print("Logging in")
        portalLogin(myid,mypass)
        print("Logged in now sleeping!")
        sleep()
        main()
    else:
        if checkLogin() == True:
            sleep() 
            main()
        else:
            while(failedLogin < 3):
                portalLogin(mypass,myid)
            if checkLogin() == True:
                
                main()
            else:
                print("Couldn't log in,check error logs")
                exit()
if __name__ == '__main__':
    main()
