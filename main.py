from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

used_words = []

driver_service = Service('D:\Code\Drivers\chromedriver.exe')
game_driver = webdriver.Chrome(service=driver_service)
dict_driver = webdriver.Chrome(service=driver_service)

# lobby = input('Lobby code? ')
# driver.get(f'https://jklm.fun/{lobby}')
game_driver.get('https://jklm.fun/BBJM')  # Hardcoded lobby (for testing)
dict_driver.get('https://www.listapalabras.com/palabras-con.php')
time.sleep(2)

# TODO: Must wait for user to join the game to proceed.

# The game screen itself is an iframe. As selenium cannot access iframe data directly, we must first switch to the frame
iframe = game_driver.find_element(By.TAG_NAME, 'iframe')  # Find iframe
game_driver.switch_to.frame(iframe)  # Switch to iframe
time.sleep(3)

game_on = True
while game_on:
    syllable = game_driver.find_element(By.CLASS_NAME, 'syllable').text  # Fetch syllable from its respective div
    inputElement = dict_driver.find_element(By.ID, 'busqueda')
    inputElement.send_keys(syllable)
    inputElement.send_keys(Keys.ENTER)

    word_found = False

    word = dict_driver.find_element(By.ID, 'palabra_resultado')
    print(word.text)
    print(used_words)
    game_on = False

game_driver.quit()
dict_driver.quit()
