# 1
# index = 1

# while index < 7: # 1 2 3 4 5 6 7
#     if index % 2 == 0: # F T F T F T
#         print("Even ", end="") # F Even F Even F Even

#     index += 1 # 2 3 4 5 6 7

# else:
#     print("done") # done


# 2
# num = 1
# while True: # T1 T2 T3 T4 T5
#     if num > 3: # F F F T T 
#         print(3, end="") # # 3 3
#     elif num > 6: # F F F
#         print(6) #
#     else:
#         print("?") # ???

#     if num >= 9: # F F F F F
#         break

#     num += 1 # 2 3 4 5 6

# output
# ?
# ?
# ?
# 333333

# 3
# def main_func(num):
#     print("Start")
#     for val in range(num): #  [0, 1, 2, 3, 4, 5]
#         print("% ", end="") #

#     for val in range(num - 2): # [0, 1, 2, 3]
#         print("$ ", end="")  #

#     print("End")    

# main_func(6)


# from random import random

# while True:
#     num = random()
#     print(num)
#     if num == 1.0:
#         break


# Problem 1
names = ["Mike", "Jennie", "Frank", "Emily", "Todd", "Maria"]

# print(names[3])
# print(names[1:5])
# print(names[-3:])
# print(names[::])
# print(names[::2])
# print(names[1::2])
# print(names[::-1])

# Problem 2
# nums = [1, 2, 3, 4]

# for num in nums:
#     if num % 2 == 0:
#         print("even", end=" ")

# else:
#     print("Done!")

# # Problem 3

people = [
    {"name": "Tom", "age": 24},
    {"name": "Rob", "age": 27},
    {"name": "Dan", "age": 35},
    {"name": "Bill", "age": 43},
    {"name": "Dominic", "age": 21},
]
ages = []
for person in people:
    if person['age'] > 25:
        ages.append(person["age"])

print(ages)