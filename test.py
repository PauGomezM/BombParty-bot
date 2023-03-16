from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

used_words = []


player_username = 'stoupeaks'

driver_service = Service('D:\Code\Drivers\chromedriver.exe')
driver = webdriver.Chrome(service=driver_service)
driver.get('https://jklm.fun/EKTW')

time.sleep(1)

inputElement = driver.find_elements(By.TAG_NAME, 'input')[1]
inputElement.send_keys(player_username)
inputElement.send_keys(Keys.ENTER)

time.sleep(3)

iframe = driver.find_element(By.TAG_NAME, 'iframe')  # Find iframe
driver.switch_to.frame(iframe)  # Switch to iframe
time.sleep(4)

while True:
    syl = driver.find_element(By.CLASS_NAME, 'syllable').text
    print(syl)

    time.sleep(3)





