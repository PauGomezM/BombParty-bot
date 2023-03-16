from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

words_list = []
used_words = []
common_misspelled_letters = 'acourhmneio'

# Save words in a list
with open(f'./es_words.txt') as file:
    words = file.readlines()

# Iterate each word to replace and remove unwanted characters
for word in words:
    word = word.replace('Ã±', 'n')
    words_list.append(word.strip())

# lobby = input('Lobby code? ')
# player_username = input('Username? ')
player_username = 'hermano'  # Hardcoded username (for testing)

driver_service = Service('D:\Code\Drivers\chromedriver.exe')
game_driver = webdriver.Chrome(service=driver_service)

# driver.get(f'https://jklm.fun/{lobby}')
game_driver.get('https://jklm.fun/RVXA')  # Hardcoded lobby (for testing)

# Enters username
inputElement = game_driver.find_elements(By.TAG_NAME, 'input')[1]
for _ in range(11):
    inputElement.send_keys(Keys.BACKSPACE)
inputElement.send_keys(player_username)
inputElement.send_keys(Keys.ENTER)
time.sleep(2)

# The game screen itself is an iframe. As selenium cannot access iframe data directly, we must first switch to the frame
iframe = game_driver.find_element(By.TAG_NAME, 'iframe')  # Find iframe
game_driver.switch_to.frame(iframe)  # Switch to iframe
time.sleep(4)

# Main game loop
repeat_flag = False
game_on = True
while game_on:

    if not repeat_flag:
        # Waits for turn
        turn = False
        while not turn:
            time.sleep(0.2)
            own_turn = game_driver.find_element(By.CLASS_NAME, 'selfTurn').is_displayed()
            if own_turn:
                turn = True

        # Fetch syllable
        syl = game_driver.find_element(By.CLASS_NAME, 'syllable').text
        syl = syl.lower()

        # Set a random words list starting point
        x = random.randint(0, 610000)
        # For each word in the list, check if it contains the desired syllable. Not accepted if already used before.
        for i in range(x, len(words_list)):
            if syl in words_list[i] and words_list[i] not in used_words:
                word = words_list[i]
                used_words.append(word)
                break

        # Sets input location in the iframe's html text
        narrowedElement = game_driver.find_element(By.CLASS_NAME, 'selfTurn')
        inputElement = narrowedElement.find_element(By.TAG_NAME, 'input')
        # Wait time to start typing
        think_time = random.uniform(0.4, 2)
        time.sleep(think_time)
        # Type each letter
        chance = random.randint(1, 100)
        repeat_flag = False
    else:
        time.sleep(0.15)
        chance = 50  # Random chance

    for i in range(len(word)):

        # Misspell case 1
        if chance == 1:
            letter_pos = random.randint(0, len(word) - 1)
            if i == letter_pos:
                i = 'c'

            inputElement.send_keys(word[i])
            time.sleep(0.1)
            repeat_flag = True

        # Misspell case 2 (WIP)
        # elif chance == 2:
        #     random_letter = random.randint(0, len(common_misspelled_letters) - 1)
        #     letter_pos = random.randint(0, len(word) - 1)
        #     if i == word[letter_pos]:
        #         i = random_letter
        #     inputElement.send_keys(i)
        #     time.sleep(0.1)

        # Correct spell (with chance to misspell mid-word)
        else:
            inputElement.send_keys(word[i])
            type_time = random.uniform(0.02, 0.2)
            time.sleep(type_time)

            # Adds chance to make mistake and backspace
            chance = random.randint(1, 35)
            if chance == 2:
                n_misspells = random.randint(1, 3)
                # misspells n amount of letters
                for _ in range(n_misspells):
                    letter = random.randint(0, len(common_misspelled_letters) - 1)
                    inputElement.send_keys(common_misspelled_letters[letter])
                    time.sleep(0.05)
                time.sleep(0.1)
                # Backspaces n amount of misspelled letters
                for _ in range(n_misspells):
                    inputElement.send_keys(Keys.BACKSPACE)
                    time.sleep(0.1)


    if not game_driver.find_element(By.CLASS_NAME, 'selfTurn').is_displayed():
        continue

    inputElement.send_keys(Keys.ENTER)

    time.sleep(1)