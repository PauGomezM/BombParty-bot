# BombParty-bot

BombParty is an online game at [jklm.fun](https://jklm.fun) where players have to provide a word that contains the given syllable before the bomb explodes. By using Selenium and several language dictionaries, this program is able to fetch data from the game, compute it, and type back an answer into the game automatically. It has been coded so that the answer is written as humanly as possible, simulating human typing and thinking.

Note: The bot misspells words from time to time. This is not a bug, it's a feature :) (We want to avoid suspicion from other players at all costs)

![game gif](https://user-images.githubusercontent.com/95043218/225719743-3de852ef-29e4-4f04-ad2c-3fb9fdd96568.gif)

Even though the game can be played in multiple languages, the bot can be configured to play Spanish and English only.

## Requirements

- Python
- Selenium
- Google Chrome or another browser supported by Selenium

The repository no longer ships a browser-driver executable. Selenium is allowed to resolve/manage the appropriate driver instead of running a binary committed to source control.

## How to use

1. Clone or download the repository.
2. Install Selenium in a virtual environment.
3. Execute `main.py`.
4. Console will prompt the user to input necessary data to join online lobby.
5. Relax and enjoy the show.

## Known issues

- If bot fails to provide a word before the time runs out, it will crash and stop the program. Game itself and the rest of players are not affected.

## Disclaimer

This has been made with the aim of getting used to web scraping and other web automation tasks with Python. This is a cheat and may get you banned.
