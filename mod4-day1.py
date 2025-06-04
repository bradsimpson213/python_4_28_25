# Sets vs List/Tuple
# nums = [1, 2, 3, 3, 4, 4, 4, 5]

# nums_set = {1, 2, 3, 3, 4, 4, 4, 5}
# print(nums_set )

# print(tuple(nums))
# print(set(nums))

# set_nums = set(nums)
# print(list(set_nums))



# Exceptions & Try/Except

def save_the_world():
    print("Avengers Assemble!")
    print('World is saved!')

num = 0
print(5/num)
try:
    print("in the try block")
    print(5/num)

except ZeroDivisionError:
    print("ZERO division error, you cannot divide by zero in math")
    print(f"Did you mean to divide 5 by 1 instead to get {5/1}")

except TypeError:
    print("We can't divide by words or letters")

# except:
#     print("You have made an error")

else:
    print("YAY! our math worked!!!")

finally:
    print("We will always see this code")



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



def lunch_picker():
    lunches = ["Wings", 'Pizza', 'Chicken Sandwich']

    lunch_choice = input("What would you like to eat for lunch today?")

    if lunch_choice not in lunches:
        raise Exception("Lunch Error we do not have that on the menu today")

    else:
        print(f"enjoy your {lunch_choice}")

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

vals = [1, 2, 3, 4, 5]
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
filter_comp_vals = [val for val in vals if val % 2 == 0]
# print(filter_comp_vals)

# File

file = open("story.txt")
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

# new_file = open(f"story.txt", 'x')

# new_file = open("morestory.txt", 'w')

# new_file.write("We were here and we wrote this! \n")

# new_file.close()

# new_file_again = open("morestory.txt", 'a')

# new_file_again.write("One more new line of text...\n")

# new_file_again.close()


# new_file_again = open("morestory.txt", 'r+')

# new_file_again.seek(40)
# # sample_line = new_file_again.readline()
# # print(sample_line)
# new_lines = [
#     "Sit right back and you'll hear a tale \n",
#     "A tale of a fatefull trip \n",
#     "That started from the topic port \n"
#     "And this tiny ship"
# ]
# new_file_again.write("New text here \n")
# new_file_again.writelines(new_lines)

# new_file_again.close()

with open("story.txt") as file:
    print("closed", file.closed)
    content = file.read()
    print(content)


# print("closed", file.closed)
# from csv import reader, DictReader

with open("sales_data.csv") as file:
    # csv_list = reader(file)
    # print(list(csv_list))
    csv_dict = DictReader(file, fieldnames=["row 1", 'row 2', 'row 3'])
    csv_list = list(csv_dict)
    csv_list.pop(0)
    print(csv_list)
    # print(csv_dict.items())


# SALES PRACTICE PROBLEM

# from csv import DictReader, writer

with open("sales_data.csv") as file:
    # csv_list = reader(file)
    # print(list(csv_list))
    csv_dict = DictReader(file)
    all_sales = DictReader(file)
    # print("all sales data", list(all_sales))

    sum_sales = {}

    for item in all_sales:
        # print("ITEM", item)
        if item["Type"] not in sum_sales:
            sum_sales[item['Type']] = int(item["Sales"])
        else:
            sum_sales[item['Type']] += int(item["Sales"])

        # print("SUMMARY", sum_sales)

    print("sum_sales", sum_sales, end='|')

    with open("summary_sales.txt", "x") as results:
        summary_data = writer(results)

        summary_data.writerow(["Category", "Total Sales"])

        for key, value in sum_sales.items():
            summary_data.writerow([key, value])



# def error_in_funct() :
#     raise Exception("This is an error")


# error_in_funct()

from csv import DictReader, writer

with open("sales_data.csv") as file:
    all_sales = DictReader(file)

    sum_sales = {}

    for item in all_sales:
        if item["Type"] not in sum_sales:
            sum_sales[item['Type']] = int(item["Sales"])
        else:
            sum_sales[item['Type']] += int(item["Sales"])

    with open("summary_sales.txt", "w") as results:
        summary_data = writer(results)

        summary_data.writerow(["Category", "Total Sales"])

        for key, value in sum_sales.items():
            summary_data.writerow([key, value])




my_dict = {
"1": "Hello",
1: "Goodbye"
}
print(my_dict["1"])
print(my_dict[1])



while True:
    index = 0
    if index == 2:
        print("Hello")
        break

    index += 1