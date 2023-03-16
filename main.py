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
# player_username = input('Username? ')

dict_driver.get('https://www.listapalabras.com/palabras-con.php')

player_username = 'hermano'  # Hardcoded username (for testing)
game_driver.get('https://jklm.fun/BBSG')  # Hardcoded lobby (for testing)

inputElement = game_driver.find_elements(By.TAG_NAME, 'input')[1]
for _ in range(11):
    inputElement.send_keys(Keys.BACKSPACE)
inputElement.send_keys(player_username)
inputElement.send_keys(Keys.ENTER)

time.sleep(3)
# TODO: Must wait for user to join the game to proceed.

# The game screen itself is an iframe. As selenium cannot access iframe data directly, we must first switch to the frame
iframe = game_driver.find_element(By.TAG_NAME, 'iframe')  # Find iframe
game_driver.switch_to.frame(iframe)  # Switch to iframe
time.sleep(1)

game_on = True
while game_on:

    turn = False
    while not turn:
        time.sleep(0.05)
        turn = game_driver.find_element(By.CLASS_NAME, 'selfTurn').is_displayed()
        if turn:
            turn = True

    syllable = game_driver.find_element(By.CLASS_NAME, 'syllable').text  # Fetch syllable from its respective div

    inputElement = dict_driver.find_element(By.ID, 'busqueda')
    inputElement.send_keys(syllable)
    inputElement.send_keys(Keys.ENTER)

    # search = True
    # i = 0
    # while search:
    #     word = dict_driver.find_elements(By.ID, 'palabra_resultado')[i]
    #     if word.text not in used_words:
    #         used_words.append(word.text)
    #         search = False
    #     i += 1

    word = dict_driver.find_element(By.ID, 'palabra_resultado')

    narrowedElement = game_driver.find_element(By.CLASS_NAME, 'selfTurn')
    inputElement = narrowedElement.find_element(By.TAG_NAME, 'input')
    inputElement.send_keys(word.text)
    inputElement.send_keys(Keys.ENTER)





