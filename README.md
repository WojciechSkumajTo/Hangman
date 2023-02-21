# Hangman

## Description
Hangman is a word game in which the player tries to guess a hidden word by guessing individual letters. Each incorrect guess results in drawing another part of a hanging man, and the player must guess the word before the hanging man is completed.

This program implements the Hangman game in Python 3. The program randomly selects a word from a list of words and places it on the board, which shows how many letters the word has. The player tries to guess the word by guessing individual letters. Each incorrect guess results in drawing another part of the hanging man. The player has a limited number of guesses to guess the word. After completing the game, the program informs the player whether they won or lost.

## Requirements
- python 3.x

## Installation
The program does not require installation. To run the program, simply download the `hangman.py`.
- Clone this repository in the terminal (or command prompt)
```shell
   git clone https://github.com/WojciechSkumajTo/Hangman.git
```
- Run the Python 3 code in the terminal (or command prompt):
```shell
  sudo python3 hangman.py
```
## Usage

To start the game, run the `hangman.py` file in the console. The player will see a board with the hidden word represented by dashes representing the unknown letters. The player can input letters to try and guess the word. After each guess, the program will inform the player whether the letter was correct or not. If the letter is correct, the program will reveal its position in the word. If the letter is incorrect, the program will draw another part of the hanging man.

The player has a limited number of guesses to guess the word. If the player fails to guess the word before exceeding the guess limit, they lose. If they guess the word, they win.

## Author
This program was written by **WojciechSkumajTo** as an example of a simple Hangman program in Python 3.
