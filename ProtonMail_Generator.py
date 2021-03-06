import os.path
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import string
import secrets
from random import randint
from selenium.webdriver.support.wait import WebDriverWait
import random
from selenium.webdriver.common.action_chains import ActionChains

# username generation
output_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(12))
username = output_string
print(username)
# end username generation

# password generation
import string
import secrets
alphabet = string.ascii_letters + string.digits
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(20))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 12):
        break
print(password)
# end password generation

# create txt file with username and password
dirname = os.path.dirname('/filepath to folder containing Python script/')
txt_path = os.path.join(dirname, 'proton_username_pw.txt')
txt_file = open(txt_path, "a")

random_int = randint(111111,999999)
txt_file.write("username: "+ username + str(random_int) + " password: " + password)
txt_file.write("\n")
txt_file.close()
username_vf = username+str(random_int)

time.sleep(1)

# ProtonMail Account Generation
driver = webdriver.Chrome()
driver.get('https://account.protonmail.com/signup?language=en')
time.sleep(6)
options = webdriver.ChromeOptions()
options.add_argument("start-maximized");
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
time.sleep(6)

#input username
from selenium.webdriver.common.keys import Keys

actions = ActionChains(driver)
text = username_vf
for character in text:
    actions.send_keys(character)
    actions.perform()
    time.sleep(0.2) # pauses for 0.2 seconds in between chars to avoid glitch

#input passwords
driver.find_element(by=By.ID, value='password').send_keys(password)
time.sleep(8)
driver.find_element(by=By.ID, value='repeat-password').send_keys(password)
time.sleep(8)
driver.find_element(by=By.XPATH, value="//button[contains(text(),'Next')]").click()
time.sleep(8)
driver.find_element(by=By.XPATH, value="//button[contains(text(),'Skip')]").click()
time.sleep(8)
driver.find_element(by=By.XPATH, value="//button[contains(text(),'Confirm')]").click()
time.sleep(8)
driver.find_element(by=By.XPATH, value="//button[contains(text(),'Select plan')]").click()
time.sleep(8)

# manually solve Captcha window after code clicks checkbox
WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@class='w100 h-custom' and @title='Captcha']")))
WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='widget containing checkbox for hCaptcha security challenge']")))
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='anchor']"))).click()