from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

used_words = []


driver_service = Service('D:\Code\Drivers\chromedriver.exe')
dict_driver = webdriver.Chrome(service=driver_service)
dict_driver.get('https://www.listapalabras.com/palabras-con.php')
time.sleep(2)


inputElement = dict_driver.find_element(By.ID, 'busqueda')
inputElement.send_keys('lol')
inputElement.send_keys(Keys.ENTER)


for i in range(10):
    word = dict_driver.find_elements(By.ID, 'palabra_resultado')
    print(word[i].text)


