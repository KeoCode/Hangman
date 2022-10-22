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
    name = input("Welcome! Please enter your Name:\n")
    play = input(f"Hi {name}, are yo ready to begin?\n")


def get_word():
    """
    Pick a random word from the list we saved into the data variable
    """
    word = random.choice(data)
    print(word)


def main():
    intro_to_game()
    get_word()

main()