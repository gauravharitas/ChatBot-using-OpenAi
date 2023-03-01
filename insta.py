
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def acinfo():
    
    with open('accountinfo.txt','r') as f:
        info=f.read().split()
        mail=info[0]
        pswd=info[1]
        


    return mail, pswd

mail,pswd = acinfo()

name="Dev Haritas"
msg="Bot message testing..."

options = Options()
options.add_argument("start-maximized")

driver=webdriver.Chrome(options=options)

driver.get("https://www.instagram.com/?hl=en")
mail_xp='//*[@id="loginForm"]/div/div[1]/div/label/input'
pswd_xp='//*[@id="loginForm"]/div/div[2]/div/label/input'
login_xp='//*[@id="loginForm"]/div/div[3]'
notnow_xp='//*[@id="react-root"]/section/main/div/div/div/div/button'
noti_notnow_xp='/html/body/div[4]/div/div/div/div[3]/button[2]'
srctabclick_xp='//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]/div'
srctab_xp='//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'
name_xp='//*[@id="f13f699a9132154"]/div/div/div'
namemsgbox_xp='//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button/div'
typemsg_xp='//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea'



time.sleep(2)

driver.find_element_by_xpath(mail_xp).send_keys(mail)
time.sleep(1)
driver.find_element_by_xpath(pswd_xp).send_keys(pswd)
time.sleep(1)
driver.find_element_by_xpath(login_xp).click()
time.sleep(5)
driver.find_element_by_xpath(notnow_xp).click()
time.sleep(5)
driver.find_element_by_xpath(noti_notnow_xp).click()
time.sleep(4)
driver.find_element_by_xpath(srctabclick_xp).click()
time.sleep(2)
driver.find_element_by_xpath(srctab_xp).send_keys(name)
time.sleep(2)
driver.find_element_by_xpath(srctab_xp).send_keys(Keys.ENTER)
driver.find_element_by_xpath(srctab_xp).send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_xpath(namemsgbox_xp).click()
time.sleep(2)
driver.find_element_by_xpath(typemsg_xp).click()
time.sleep(2)
driver.find_element_by_xpath(typemsg_xp).send_keys(msg)
time.sleep(2)
driver.find_element_by_xpath(typemsg_xp).send_keys(Keys.ENTER)