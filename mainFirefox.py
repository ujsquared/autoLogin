import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException as ecp
service = Service('/snap/bin/geckodriver')
def sleep():
    time.sleep(3600)
def checkLogin():
    try:
        with webdriver.Firefox(service=service) as driver:
            wait = WebDriverWait(driver, 30)
            driver.get("https://192.168.1.250/connect/PortalMain")
            loggedInText = 'Welcome to the network.'
            driver.find_element(By.CSS_SELECTOR,"#nac_expiration_time")
            print("Logged in Already")
            return True
    except  ecp:
        print("Not found, ecp error raised")
        return False
    else:
        print("Different Error raised, check logs")
        print(Exception)
        return False

def portalLogin(userId, password):
    try:
        with webdriver.Firefox(service=service) as driver:
            driver.get("https://192.168.1.250/connect/PortalMain")
            wait = WebDriverWait(driver, 30)
            wait.until(presence_of_element_located((By.CSS_SELECTOR,'#LoginUserPassword_auth_username.formInput')))
            driver.find_element(By.CSS_SELECTOR,'#LoginUserPassword_auth_username.formInput').send_keys(userId + Keys.RETURN)
            wait.until(presence_of_element_located((By.CSS_SELECTOR,'#LoginUserPassword_auth_password')))
            driver.find_element(By.CSS_SELECTOR,'#LoginUserPassword_auth_password').send_keys(password + Keys.RETURN)
            time.sleep(3)
    except ecp:
        print("login failed, ecp raised!")
def main():
    failedCheck = 0
    failedLogin = 0
    myid = 'B323049'
    mypass = 'B323049'
    check = checkLogin()
    if check is True:
        ("Already logged in!")
        sleep()
        main()
    elif check is False:
        print("Logging in")
        portalLogin(myid,mypass)
        print("Logged in now sleeping!")
        sleep()
        main()
    else:
        if checkLogin() is True:
            sleep() 
            main()
        else:
            while(failedLogin < 3):
                portalLogin(mypass,myid)
            if checkLogin() is True:
                
                main()
            else:
                print("Couldn't log in,check error logs")
                exit()
if __name__ == '__main__':
    main()   

