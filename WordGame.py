#Word Game is a knock-off version of a popular online word-guessing game.
#WordGame.py
#Name: Talia Astorino
#Date: 02/21/2026
#Purpose: Complete a 5-letter word guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    return letter in word

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""
    return word[spot] == letter

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""

    result = ""
    myGuess = myGuess.upper()
    word = word.upper()

    for i in range(len(myGuess)):
        letter = myGuess[i]
    
        if inSpot(letter, word, i):
            result = result + letter
        elif inWord(letter, word):
            result = result + letter.lower()
        else:
            result = result + "*"

    return result
def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList).upper()
    print(todayWord)

    #User should get 6 guesses to guess
    attempts = 6

    while attempts > 0:
        guess = input("Enter a 5-letter word: ").upper()

        if len(guess) != 5:
            print("Please enter exactly 5 letters.")
            continue

        feedback = rateGuess(guess, todayWord)
        print("Feedback:", feedback)

        if guess == todayWord:
            print("You guessed it!")
            return

        attempts = attempts - 1
        print("Attempts remaining:", attempts)

    print("Game over! The word was:", todayWord)
  
if __name__ == '__main__':
  main()
