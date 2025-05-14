# FUNCTIONS

# print("Hello Nicole")
# print("How are you doing today?")
# print("Hello Brad")
# print("How are you doing today?")
# print("Hello Kantrell")
# print("How are you doing today?")
# print("Hello Davon")
# print("How are you doing today?")

def greet(name="friend") -> str:
    """a function that takes in an optional person's 
    name as a string and returns a string greeting"""
    # print(name)
    # print(f'Hello {name}!')
    greeting = f"Hello {name}"
    print("Whats up?")
    return greeting

# print("Hello Nicole!")
print(greet("Brad"))
# print("Hello Brad!")
print(greet("Kantrell"))
print(greet("Davon"))
print(greet())

# help(greet)


# METHOD
# name = "brad"
# print(name.upper())

# CLASSES 
# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def hello(self, name="friend"):
#         print(f"Hello {name}")
    
#     def bye(self):
#         print("Bye!")


# person = Human("Brad", 47)
# person.hello()
# person = Human("Davon", 21)
# person.helLo()

# human = {
#     "name": "Brad",
#     "age": 47 
# }

# human_2 = {
#     "name": "Davon",
#     "age": 21
# }


# person = "Brad"


# def is_even(integer) -> bool :
#     """ function that accepts and integer and 
#     returns a boolean on whether the number is 
#     even or not"""
#     # helpful comment
#     # calc = integer % 2 == 0
#     # print(calc)
#     return integer % 2 == 0

# print(is_even(6))
# print(is_even(7))
# help(is_even)


# def summarizer(num1, num2, num3=10):
#     """Given a mix of different parameters, 
#     this function will calculate their sum"""
#     total = num1 + num2 + num3
#     return total

# print(summarizer(1, 5, 4))
# print(summarizer(num3=5, num1=1, num2=4))
# print(summarizer(1, 5))
# print(summarizer(1, 5, 100))

# SCOPE

num_1 = 20
PII = 3.145

print("Global 1", num_1)

def function():
    # num_1 = 30
    global num_1
    print("Inside function", num_1)
    num_1 += 10
    print(PII)
    print("Inside function 2", num_1)

function()


print('Global 2', num_1)




# # other way to do the above
# num_1 = 20
# PII = 3.145

# print("Global 1", num_1)

# def function():
#     # num_1 = 30
#     num_1 = 20
#     print("Inside function", num_1)
#     num_1 += 10
#     print(PII)
#     print("Inside function 2", num_1)
#     return num_1

# num_1 = function()

# print('Global 2', num_1)

# def function2():
#     num_1 = 40
#     print("Inside second function", num_1)

# function2()


# def my_func(int):
#     print(int)
#     val = int(3.23)

# my_func(1)

# num = int("1234")
# print(num)

# Built in function

# nums = [1, 2, 3, 4, 5]

# print(sum(nums))
# print(min(nums))
# print(max(nums))



# def sum(list1):
#     total = 0
#     for num in list1:
#         total += num
#     return total


# def min1(list1):
#     low = 100
#     for num in list1:
#         if num < low:
#             low = num

#     return low

# print(min1([ 2, 3, 4, 5, 1]))
# print(total)

# print(round(3.145, 0))
# print(abs(300))
# print(abs(-300))

# print(len("brad"))
# print(len([1, 2, 3, 4]))
# print(len((1, 2, 3)))

# print('Brad')
# print(list("Brad"))


names = ["JAMES", "julie", "Ana", "Ria"]
# # sorted_names = sorted(names, reverse=True)
def case_maker(val):
    return val.upper()

# data after key applied
names1 = ['JAMES', 'JULIE', 'ANA', "RIA"]

# sorted_names_og = sorted(names)
sorted_names = sorted(names, key=case_maker)
# print(sorted_names_og)
# print(sorted_names)

stuff = [[1, 7, 3],
         [2, 6, 4],
         [3, 5, 5],
         [4, 4, 6],
         [5, 3, 7],
         [6, 2, 8]]


# def indexer(lst):  [1, 7, 3]
#     return lst[1]

# def list_indexer(list1):
#     return list1["age"]

# stuff_rev = [7, 6, 5, 4, 3, 2]

# print(sorted(stuff, key=list_indexer))
# people = [
#     {
#         "name": "Brad",
#         "age": 47
#     },

#     {
#         "name": "Davon",
#         "age": 24
#     }
# ]

# CALCULATOR

def addition(num_1, num_2):
    """add the 2 parameters and returns the sum"""
    return f"{num_1} + {num_2} = {num_1 + num_2}"

def subtraction(num_1, num_2):
    """subtract num_2 from num_1 and return the result"""
    return f"{num_1} - {num_2} = {num_1 - num_2}"

def multiplication(num_1, num_2):
    """multiply num_1 and num_2 and return the result"""
    return f"{num_1} * {num_2} = {num_1 * num_2}"

def division(num_1, num_2):
    """divide num_1 by num_2 and return the result"""
    return f"{num_1} / {num_2} = {num_1 / num_2}"

def calculator():
    """a simple calculator that will accept 2 numbers and 
    preform + - * / on those numbers"""
    
    print('Welcome to the calculator app!')

    calc_on = True

    while calc_on:
        num_1 = float(input("Please enter the first number: "))
        operator = input("Pick your operator ('+', '-', '*', '/'): ")
        num_2 = float(input("Please enter the second number: "))

        if operator == "+":
            # print(f"{num_1} + {num_2} = {num_1 + num_2}")
            print(addition(num_1, num_2))
        elif operator == "-":
            print(subtraction(num_1, num_2))
        elif operator == "*":
            print(multiplication(num_1, num_2))
        elif operator == "/":
            print(division(num_1, num_2))
        else:
            print("Incorrect operator choice, try again!")
            continue
        
        again = input("Do you want do make another calculation? [Y or N]: ")  # .lower()  # Y y N n 
        if again == 'y' or again == "Y":
            continue
        else:
            calc_on = False

    print('Thanks for using our calculator!')


# calculator()

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not True)
print(not False)

print(True != False) 