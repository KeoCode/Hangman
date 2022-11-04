"""
Import the random choice function and gspread to access our spreadsheet
"""
import string
import random
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

"""
Assign credentials from our API's and access our words spreadsheet
"""
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("hangman_words")

wordlist = SHEET.worksheet("wordsheet")
scoreboard = SHEET.worksheet("scores")
data = wordlist.get_all_values()
score = 0


def intro_to_game():
    """
    Welcome them to the game and get their username.
    let the press a key when they are ready to start playing
    """
    print("  /\\  /\\ __ _  _ __    __ _  _ __ ___    __ _  _ __ ")
    print(" / /_/ // _` || '_ \\  / _` || '_ ` _ \\  / _` || '_ \\ ")
    print("/ __  /| (_| || | | || (_| || | | | | || (_| || | | |")
    print("\\/ /_/  \\__,_||_| |_| \\__, ||_| |_| |_| \\__,_||_| |_|")
    print("                      |___/                          ")

    username = " "
    while True:
        username = input("Welcome! Please enter your Name: \n")

        if username.isalnum() is not True:
            print("Error: Letters and numbers only.")
            continue
        else:
            print(f"Hi {username}, You have upto 6 guesses to guess the Word.")
            input("When you are ready to play, Press the Enter key to start")
            return username

    print(f"Hi {username}, You have upto 6 guesses to guess the Secret Word.")
    input("When you are ready to play, Press the Enter key to start")
    return username


print("Error: Letters and numbers only.")


def get_word():
    """
    Pick a random word from the list we saved into the data variable
    """
    return random.choice(data)


def replay():
    """
    once game is finished, ask player if they would like to play again,
    if so restart play game function, if not then print message
    """
    replay_answer = input("would you like to play again? Enter Y/N \n").lower()
    if replay_answer == "y":
        play_game()
    else:
        print("Thanks for playing! Hope to see you again soon!")


def play_game():
    """
    Main Function for the game play. it will print out the length of is
    in the word and check if guesses are correct and reveal if they are.
    will also check how many lives you have and print message if you
    win or lose
    """
    word_string = str(get_word())
    global score

    for letter in string.punctuation:
        word_string = word_string.replace(letter, "")

    word = list(word_string)

    # sets up variables to start the game
    lives = 6
    guesses = []
    complete = False
    print(len(word) * "_ ")

    # While the Secret word has not been completed and the user still has lives
    # It displays the guesses already made and how many lives the user has left
    while complete is False and lives > 0:
        print("The word contains", len(word), "letters.")
        print("Already Guessed: ", end=" ")
        print(*guesses, sep=", ")
        print()
        guess = input(f"Lives left:{lives}, Guess a letter or the word: \n")
        print()

        # If the input is in the alphabet and is only one letter or the length
        # of the word then check if it is in the word or is the word
        # Print error if not in the alphabet or is not avalid value input.

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

        # if the letters is in word print it in its place and add to guesses
        current = ""
        if complete is False:
            for letter in word:
                if letter in guesses:
                    current += letter
                else:
                    current += "_ "
            print(current)

        # if word is completed correctly then display 'you win'
        # if they run out of lives display 'game over'
        if current == word_string:
            print("Congradulations! You got it right!")
            print("                  __    __ _       ")
            print("/\\_/\\___  _   _  / / /\\ \\ (_)_ __  ")
            print("\\_ _/ _ \\| | | | \\ \\/  \\/ / | '_ \\ ")
            print(" / \\ (_) | |_| |  \\  /\\  /| | | | |")
            print(" \\_/\\___/ \\__,_|   \\/  \\/ |_|_| |_|")
            print()
            print(f"The word is {word_string.capitalize()}")
            print()
            complete = True
            score += 10
            replay()
            return score
        elif lives == 0:
            print("Oh no! Game over!")
            print("   ___                         ___                 ")
            print("  / _ \\__ _ _ __ ___   ___    /___\\__   _____ _ __ ")
            print(" / /_\\/ _` | '_ ` _ \\ / _ \\  //  //\\ \\ / / _ \\ '__|")
            print("/ /_\\\\ (_| | | | | | |  __/ / \\_//  \\ V /  __/ |   ")
            print("\\____/\\__,_|_| |_| |_|\\___| \\___/    \\_/ \\___|_|   ")
            print()
            print(f"The Secret Word was {word_string.capitalize()}")
            print()
            score -= 10
            replay()
            return score


def update_scores(username, final_score):
    """
    Add 10 points when complete the game and lose 10 points if lose the game.
    Update the score to scoreboard
    """
    scoreboard.append_row([username, final_score])
    print(f"Final Score: {final_score}")


def main():
    """
    All the main function of game play in order
    """
    username = intro_to_game()
    final_score = play_game()
    update_scores(username, final_score)


if __name__ == "__main__":
    main()
