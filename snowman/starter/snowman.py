# Game Planning
# guesses or input
# randomly choose a word
# prints - user what happened
# loop or iterate
# if statement logic
# helper function

from logo import logo
from stages import snowman as stages
from random import choice
import os


def get_game_word() -> str:
    """ open the words text file, read them in, 
    clean the data, and randomly choose a word and return it"""

    file = open("words.txt")

    # def remove_whitespace(word):
    #     return word.rstrip()
    
    # cleaned_words = map(remove_whitespace, file)
    cleaned_words = [ word.rstrip() for word in list(file)]
    return choice(list(cleaned_words))


def printer(chances, display, guesses, error=None) -> None:
    """helper function for printing"""
    if error:
        print(error)

    print(stages[chances])
    print(" ".join(display))
    if guesses:
        print(f"You have guessed: {guesses}")


def handle_guess(stages, chances, display, guesses) -> str:
    """helper function to handle user guesses"""
    bad_guess = True

     # while loop for guessing
    while bad_guess:
        user_guess = input('Guess a letter: ').lower()
        os.system("cls")

        if len(user_guess) != 1:
            error = f"We can only guess a single letter, not {user_guess}, try again, no penalty. "
            printer(chances, display, guesses, error)
            continue
        
        if user_guess not in 'abcdefghijklmnopqrstuvwxyz':
            error = F"You can only guess letters, not {user_guess}, try again, not penalty"
            printer(chances, display, guesses, error)
            continue

        if user_guess in guesses:
            error = F"You already guessed {user_guess}, try again, not penalty"
            printer(chances, display, guesses, error)
            continue

        bad_guess = False
        return user_guess



def play_snowman() -> None:
    """ plays the snowman game"""

    os.system("cls")
    print(logo)
    print("Welcome to Snowman!")
    print("🎵🎶 DO YOU WANT TOI MELT A SNOWMAN!!!🎵🎶")
    print("Guess the word before the snowman melts...💧")
    winning_word = get_game_word()
    chances = 0
    guesses = set()

    display = ["_" for _ in range(len(winning_word))]
    # display = []
    # for letter in range(len(winning_word)):
    #     display.append("_")
    # _ _ _ _ _ 
    # print(stages[chances])

    # print(" ".join(display))
    printer(chances, display, guesses)

    # for debugging only
    print(winning_word)

    play = True

    # while loop for playing
    while play:

        bad_guess = True

        # while loop for guessing
        user_guess = handle_guess(stages, chances, display, guesses)
        guesses.add(user_guess)
            
        # shock
        # h
        # _h___
        for index, letter in enumerate(winning_word):
            if letter == user_guess:
                display[index] = letter.upper()

        if user_guess not in winning_word:
            chances += 1
            print(f"Sorry, {user_guess.upper()} was not in the game word...")
            if chances == 6:
                os.system("cls")
                print(stages[-1])
                play = False
                print(F"You lost: The word was {winning_word.upper()}.  POOR FROSTY💧💧💧")
                # play again functionality
                return 
            

        printer(chances, display, guesses)


        if "_" not in display:
            play = False
            print(f"{winning_word.upper()} was the word!  YOU WIN!  FROSTY LIVES! ☃️")
            # play again functionality
            return


play_snowman()

# LIST COMPREHENSIONS

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# copy_nums = [num for num in nums]
# second_copy_nums = [*nums]
# print(copy_nums)
# print(second_copy_nums)
# double_nums = [ num * 2 for num in nums ]
# print(double_nums)
# even_nums = [ num * 2 for num in nums if num % 2 == 0 ]
# print(even_nums)