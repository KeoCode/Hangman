"""
Import the random choice function and gspreadto access our spreadsheet of words
"""
import string
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
    input("when you are ready to play, Press the Enter key to start")


def get_word():
    """
    Pick a random word from the list we saved into the data variable
    """
    return random.choice(data)


def play_game():
    """
    Main Function for the game play. it will print out the length of is
    in the word and check if guesses are correct and reveal if they are.
    will also check how many lives you have and print message if you
    win or lose
    """
    word_string = str(get_word())

    for letter in string.punctuation:
        word_string = word_string.replace(letter, '')

    word = list(word_string)
    # print(word)

    lives = 6
    guesses = []
    complete = False
    print(len(word) * '_ ')

    while complete is False and lives > 0:
        print('The word contains', len(word), 'letters.')
        print(guesses)
        print()
        guess = input(f"Lives left:{lives}, Guess a letter or the word: ")
        print()

        if guess.isalpha():
            if len(guess) == 1:
                if guess in guesses:
                    print(f"you have already guessed {guess.upper()}.")
                    print()
                elif guess not in word:
                    print(f"Sorry, {guess.upper()} is not in the Secret Word")
                    guesses.append(guess)
                    print()
                    lives -= 1
                elif guess in word:
                    print(f"Great! The letter {guess.upper()} is in the word")
                    guesses.append(guess)
                    print()
                else:
                    print("Error: Oops, please check your entry")
                    print()
            elif len(guess) is len(word):
                if guess == word:
                    print(f"Well done! You guessed the correct Word {word}")
                    complete = True
                else:
                    print(f"Sorry, {guess.upper()} is not the word!")
                    lives -= 1
            else:
                print("Oops! The amount of letters is not right.")

        else:
            print("ValueError: Please enter a letter or guess the word.")
            lives -= 1

        current = ''
        if complete is False:
            for letter in word:
                if letter in guesses:
                    current += letter
                else:
                    current += '_'
            print(current)

        # for i in word:
        #     if i.lower() in guesses:
        #         print(i, end="")
        #     else:
        #         print("_", end="")
        # print("")

    #     guesses.append(guess.lower())
    #     if guess.lower() not in word:
    #         lives -= 1
    #         print(f" Guessed already: {guesses}")
    #         if lives == 0:
    #             break

    # complete = True
    # for i in word:
    #     if i.lower() not in guesses:
    #         complete = False

    if current is word_string:
        print("Congradulations! You got it right!")
        print(f"The word is {word_string.capitalize()}")
        print()
        complete = True
    elif lives == 0:
        print("Oh no! Game over!")
        print(f"The Secret Word was {word_string.capitalize()}")
        print()


def replay():
    """
    once game is finished, ask player if they would like to play again,
    if so restart play game function, if not then print message
    """
    replay_answer = input("would you like to play again? Enter Y/N ").lower()
    if replay_answer == 'y':
        play_game()
    else:
        print("Thanks for playing! Hope to see you again soon!")


def main():
    """
    All the main function of game play in order
    """
    intro_to_game()
    play_game()
    replay()


main()
