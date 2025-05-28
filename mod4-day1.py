# Sets vs List/Tuple
# nums = [1, 2, 3, 3, 4, 4, 4, 5]

# nums_set = {1, 2, 3, 3, 4, 4, 4, 5}
# print(nums_set )

# print(tuple(nums))
# print(set(nums))

# set_nums = set(nums)
# print(list(set_nums))



# # Exceptions & Try/Except

# def save_the_world():
#     print("Avengers Assemble!")
#     print('World is saved!')



# num = 0

# try:
#     print("in the try block")
#     print(5/num)

# except ZeroDivisionError:
#     print("ZERO division error, you cannot divide by zero in math")
#     print(f"Did you mean to divide 5 by 1 instead to get {5/1}")

# except TypeError:
#     print("We can't divide by words or letters")

# # except:
# #     print("You have made an error")

# else:
#     print("YAY! our math worked!!!")

# finally:
#     print("We will always see this code")



# save_the_world()
# print(num1)

# def iterate(vals):
#     if len(vals) == 0:
#         return
    
#     print(vals[0])
#     return iterate(vals[1:])

# iterate([1, 2, 3, 4, 5])

# 1. iterate([1, 2, 3, 4, 5]) ->  print(1)
# 2. iterate([2, 3, 4, 5]) -> print(2)
# 3. iterate([3, 4, 5]) -> print(2)
# 4. iterate([4, 5]) -> print(2)
# 5. iterate([5]) -> print(2)
# 6. iterate([])
# def lunch_picker():
#     lunches = ["Wings", 'Pizza', 'Chicken Sandwich']

#     lunch_choice = input("What would you like to eat for lunch today?")

#     if lunch_choice not in lunches:
#         raise Exception("Lunch Error we do not have that on the menu today")

#     else:
#         print(f"enjoy your {lunch_choice}")

# lunch_picker()

import random


def guess():
    bad_guess = True
    while bad_guess:
        try:
            user_guess = int(input("Guess a number between 1 and 20: "))

        except ValueError:
            print("We must enter numbers for our guesses")

        else:
            bad_guess = False
            return user_guess


def guessing_game():
    print("Welcome to the guessing game!")
    winning_guess = random.randint(1, 20)
    # print("WIN NUM", winning_guess)

    guesses = 5

    while guesses > 0:
        # user_guess = int(input("Guess a number between 1 and 20: "))
        user_guess = guess()
        print(user_guess)
        guesses -= 1

        if user_guess == winning_guess:
            print(f"You guessed correct! The number was {winning_guess}! You used {5 - guesses} guess.")
            return True

        elif user_guess > winning_guess:
            print(f"You guessed too high! Try again, you have {guesses} guesses left")
        
        else:
            print(f"You guessed too low! Try again, you have {guesses} guesses left")

    print(f'You have used up all your guesses.  Sorry you lost.  The number was {winning_guess}')


# print(guessing_game())


# List Comprehensions

# vals = [1, 2, 3, 4, 5]
# names = ["brad", 'nicole', 'davon', 'cieneh']
# copy_vals = [val for val in vals]
# print(copy_vals)

# mapped_vals = map(lambda val: val * 2, vals)
# print(list(mapped_vals))
# mapped_comp_vals = [ val * 2 for val in vals]
# print(mapped_comp_vals)
# cap_names = [ name + "'s" for name in names]
# print(cap_names)

# filter_vals = filter(lambda val: val %2 == 0, vals)
# print(list(filter_vals))
# filter_comp_vals = [val * 2 for val in vals if val % 2 == 0]
# print(filter_comp_vals)

# File

file = open("story.txt", 'r')
# print(file)
# print(list(file))

# for val in list(file):
#     print(val)
# content = file.read()
# print(content)
# print(file.seek(12))
# more_content = file.read()
# print(more_content)

# line_content = file.readline()
# print(line_content)
# line_content2 = file.readline()
# print(line_content2)

# all_lines = file.readlines()
# print(all_lines)
# print("file closed", file.closed)
# file.close()
# print("file closed", file.closed)

# clean_lines = [line.rstrip() for line in all_lines]
# print(clean_lines)

# for line in clean_lines:
#     print(line)

# file2 = open("story.txt", 'r+')

# # file2.seek(0)
# line_content = file2.readline()
# print(line_content)




# This is a lovely story
# about a cat...
# And then there was a dog
# and he was there too...
# and then there was also a mouse...

new_file = open("morestory.txt", 'w')

new_file.write("We were here and we wrote this! \n")

new_file.close()

new_file_again = open("morestory.txt", 'a')

new_file_again.write("This will be a new line of text")

new_file_again.close()


new_file_again = open("morestory.txt", 'r+')

new_file_again.seek(40)
# sample_line = new_file_again.readline()
# print(sample_line)
new_lines = [
    "Sit right back and you'll hear a tale \n",
    "A tale of a fatefull trip \n",
    "That started from the topic port \n"
    "And this tiny ship"
]
# new_file_again.write("New text here")
new_file_again.writelines(new_lines)

new_file_again.close()