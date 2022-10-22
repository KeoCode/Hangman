"""
Import the random choice function and gspreadto access our spreadsheet of words
"""
import random
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

"""
Assign credentials from our API's and access our words spreadsheet
"""
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_words')

wordlist = SHEET.worksheet('wordsheet')

data = wordlist.get_all_values()


def intro_to_game():
    """
    Welcome them to the game and get their username.
    let the press a key when they are ready to start playing
    """
    username = input("Welcome! Please enter your Name:\n")
    print(f"Hi {username}, You have upto 6 guesses to guess the Secret Word.")
    input("when you are ready to play, Press any key to start")


def get_word():
    """
    Pick a random word from the list we saved into the data variable
    """
    word = random.choice(data)
    return word


def play_game():
    """
    Main Function for the game play. it will print out the length of letters
    in the word and check if guesses are correct and reveal if they are.
    will also check how many lives you have and print message if you
    win or lose
    """
    word = get_word()
    lives = 6
    guesses = []
    complete = False

    while not complete:
        for letter in word:
            if letter.lower() in guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("")

        guess = input(f"Lives left:{lives}, Guess again:")
        guesses.append(guess.lower())
        if guess.lower() not in word:
            lives -= 1
            if lives == 0:
                break

    complete = True
    for letter in word:
        if letter.lower() not in guesses:
            complete = False

    if complete:
        print(f"Congrads! You got it! You guessed the Secret word {word}")
    else:
        print(f"Oh no! Game over! The Secret Word was {word}")


def main():
    """
    All the main function of game play in order
    """
    intro_to_game()
    play_game()


main()
