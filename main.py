<<<<<<< Updated upstream
=======
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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
def portalLogin(userid, password):
    options = Options()
    options.add_argument('headless')
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),options=options)
    driver.get("https://192.168.1.250/connect/PortalMain")
    oginElement = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#LoginUserPassword_auth_username.formInput')))
    loginElement = driver.find_element(By.CSS_SELECTOR,'#LoginUserPassword_auth_username.formInput')
    loginElement.send_keys(userid)
    loginElement = driver.find_element(By.ID,'LoginUserPassword_auth_password')
    loginElement.send_keys(password)
    loginButton = driver.find_element(By.ID,'UserCheck_Login_Button_span')
    loginButton.click()
portalLogin('B323049','B323049')


>>>>>>> Stashed changes
