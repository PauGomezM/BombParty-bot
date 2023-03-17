# BombParty-bot

[BombParty](https://jklm.fun) is an online game where players have to provide a word that contains the given syllable before the bomb explodes. By using Selenium and several language dictionaries, this program is able to fetch data from the game, compute it, and type back an answer into the game automatically. It has been coded so that the answer is written as humanly as possible, simulating human typing and thinking.
Moreover, there is a chance that the bot will misspell words in order to avoid suspicion from other players/parties.

![game gif](https://user-images.githubusercontent.com/95043218/225719743-3de852ef-29e4-4f04-ad2c-3fb9fdd96568.gif)

Even though the game can be played in multiple languages, the bot can be configured to play Spanish, German or English only.

## Requirements

- Selenium: Used to automate navigator. It helps fetching syllable data, and typing the word back to the game when it has been computed.

## Known issues

- If bot fails to provide a word before the time runs out, it will crash and stop the program. Game itself and the rest of players are not affected.

## Disclaimer

This has been made with the aim of getting used to web scraping and other web automation with Python. It is a cheat and may get you banned.
