
# print(4 == 4.0)
# print(4 is 4.0)


# print(True == 1)
# print(False == 0)
# print(True is 1)
# print(True is True)

# num_1 = True
# num_2 = 1 

# string = "hello"

# lunches = ["sandwich", "salad", "tacos" ]

# for lunch in lunches:
#     print(lunch.upper())

# print("salad" in lunches)
# print("soup" in lunches)

# nums = range(6)
# print(list(nums))

# for index in range(len(lunches)):
#     print(lunches[index])
#     print(lunches[index] > lunches[index + 1])




# for i in range(5): #[0, 1, 2, 3, 4]
#     if i > 3:
#         print("&")


# print(int(10/2))

# pizza = (4+2) // 2 - 1
# # PEMDAS   8   
# if pizza <= 1:
#     print("O", end="")
# if pizza >= 3:
#     print("OO", end="")
# else:
#     print("OOO", end="")

# index = 1  # 1 2 3 4 5 6

# while index < 6: # 1T 2T 3T 4T 5T 6F
#     if index % 2 == 0:  # 1F 2T 3F 4T 5F
#         print("$", end="") # $$

#     index += 1  # 2 3 4 5 6
# else:
#         print("!") # !

import os
from time import sleep
# import random 

# count = 99
# PII_2 = 3.14

# while count < 1000:
#     os.system("cls")
#     print(f"{count} little bugs in our code...")
#     sleep(2.5)
#     print(f"{count} pesky little bugs...")
#     sleep(2.5)
#     print("Take one down and patch it around...")
#     sleep(2.5)
#     new_bugs = random.randint(1, 100)
#     print("NEW BUGS",new_bugs)
#     count += new_bugs
#     print(f"{count} little bugs in our code!")
#     sleep(2.5)


# guessing GAME

import random


def guessing_game():
    print("Welcome to the guessing game!")
    winning_guess = random.randint(1, 20)
    print("WIN NUM", winning_guess)

    guesses = 5

    while guesses > 0:
        user_guess = int(input("Guess a number between 1 and 20: "))
        print(user_guess)
        guesses -= 1
        guesses = guesses - 1

        if user_guess == winning_guess:
            print(f"You guessed correct! The number was {winning_guess}! You used {5 - guesses} guess.")
            return True

        elif user_guess > winning_guess:
            print(f"You guessed too high! Try again, you have {guesses} guesses left")
        
        else:
            print(f"You guessed too low! Try again, you have {guesses} guesses left")

    print(f'You have used up all your guesses.  Sorry you lost.  The number was {winning_guess}')


print(guessing_game())


# print(10 / 3, end="")
# print(10 // 3, 10 % 3, end="")

