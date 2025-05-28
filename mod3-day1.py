# Module 3 Structured Data

# Lists
# my_list = [1, 2, 3, True, None, "Hello"]
# my_list2 = []
# my_list3 = ['wings', 'pizza', 'salad', 'sandwich', "burger"]
# my_string = "Brad"
# my_string = "Nicole"
# # LIST INDEXING
# print(my_list3)
# print(my_list3[1])
# print(my_list3[-1])
# print(my_list3[1:2])
# print(my_list3[::2])
# print(my_list3[::-1])
# print(my_list[1:-2])
# print(my_list3[start:stop:step])


# help('list')

# LIST METHODS
# foods = ['wings', 'pizza', 'salad', 'sandwich', "burger"]

# food = 'wings'
# food = "burger"

# foods.append("soup")
# print(len(foods))
# print(foods)
# foods.extend(["gyro", "taco"])
# print(foods)
# foods.remove("gyro")
# print(foods)
# foods.insert(1, "pita")
# print(foods)
# foods.insert(2, "burrito")
# print(foods)
# removed_item = foods.pop(1)
# print(f"You just removed {removed_item} from the list")
# print(foods)
# print(removed_item)
# print(len(foods))


# sort vs sorted
# print(foods.sort(reverse=True))
# print(foods)
# sorted_foods = sorted(foods)
# print(tuple(sorted_foods))


# ITERATING
# foods = ['wing', 'pizza', 'salad', 'sandwich', "burger"]

# for food in foods:
#     print(food + "s")

# print("wing" in foods)
# print("donut" in foods)
# print(list(range(len(foods))))

# for index in range(len(foods)):
#     print(f"{index + 1}. {foods[index]}")
#     if index > 0:
#         print(f"{foods[index -1]} is not the same as {foods[index]}")


# index = 1
# while index < len(foods):
#     print(f"{index + 1}. {foods[index]}")
#     if index > 0:
#         print(f"{foods[index -1]} is not the same as {foods[index]}")
#     index += 1


image_data = [
    [[25, 50, 75],
     [25, 50, 75],
     [50, 75, 100]],
    [[30, 35, 250],
     [],
     []],
    [[40, 45, 90],
     [],
     []],
]
# print(image_data[0][0][0])


# Tuples
my_tuple = (1, 2, 3, False, "Bye")
my_other_tuple = 2, 3, 4, 5
# print(my_other_tuple)

empty_tuple = ()
single_val_tuple = 1,  # or (1, )

tup = ("red", "blue")
tup = ("yellow", "green")  # no error, this works
# print(tup)                 # ("yellow", "green")
tup += tup + ("red", "blue")    # no error, this works
# print(tup)    


# print(tup[1:3])

# for color in tup:
#     print(color)

# sorted_colors = sorted(tup)
# print(tuple(sorted_colors))

# print(enumerate(tup))
# print(list(enumerate(tup)))
# print(tuple(enumerate(tup)))
# print(list(enumerate(tup)))

for index, value in enumerate(tup, 1):
    print(f"{index}. {value}")


# def sum_and_average(nums) -> tuple:
#     """takes in a list of numbers and returns 
#     the sum and average as a tuple"""
#     nums_sum = sum(nums)
#     nums_avg = nums_sum / len(nums)
#     return (nums_sum, nums_avg)

# vals = [1, 2, 3, 4, 5]
# vals_sum, vals_avg = sum_and_average(vals)
# print(vals_sum, vals_avg)



# num_1, num_2, _ = (1, 2, 3)
# print(num_1, num_2)

DAYS = ("Mon", "Tues", "Wed", "Thurs", "Fri")

def in_function(iterable, value) -> list:
    """how the built in "IN" keyword works"""
    found = False

    for item in iterable:
        if item  == value:
            found = True
            break

    return found

print("Wed" in DAYS)
print(in_function(DAYS, "Wed"))
# DAYS = "Bleh"


# def summer(num_1, num_2, num_3=10, *args):
#     total = 0
#     total += (num_1 + num_2 + num_3)
#     print(args)
#     for arg in args:
#         total += arg
#     return total

# print(summer(5, 10, 15, 20, 25, 30, 35, 46))
# print(summer(5, 10, 15))


# Dictionary
my_dict = {
    "name": 'Brad',
    "age": "old",
    4: "the number 4",
    1: "one",
    True: "one",
    (1,2): "tuple good for grids",
}

# print(my_dict["name"])
# # print(my_dict["age"])
# # my_other_dict = {"name": "Brad", "age": 47}
# # print(my_dict['hello'])
# print(my_dict.get("age"))
# print(my_dict.get("hello", "You did not find the key!"))
# # my_dict["Hello"] = "hi there!"
# my_dict["Hello"] = "not hi there"

# if my_dict.get("Hello") == None:
#     my_dict["Hello"] = "hi there!"

# else:
#     print("KEY ALREADY EXISTS")

# print(my_dict)
# del my_dict["Hello"]
# print(my_dict)

# def save_the_world():
#     print("World saved, Avengers rule!")

# save_the_world()


# my_table = [
#     {"sales": 10, "date": "Monday"},
#     {"sales": 15, "date": "Tuesday"}
# ]

users = {
    "Brad": {"name": "Brad", "age": 47},
    "Nicole": {"name": "Nicole", "age": 25},
    "Terrell": {"name": "Terrell", "age": 25},
    "Davon": {"name": "Davon", "age": 25},
    "Cieneh": {"name": "Cieneh", "age": 25},
}

# help("dict")
# print(users.keys())
# print(users.values())
# print(users.items())

# for key, user in users.items():
#     print(key, user)


# print(users["Brad"])

posts = [
    {"date": "3/14/25", "caption": "That lunch looks great!", "user": users["Brad"]},
    {"date": "5/12/25", "caption": "Python is so fun", "user": users["Nicole"]},
    {"date": "4/1/25", "caption": "Dictionaries are cool!", "user": users["Terrell"], "comments": ["yay", "great!"]},
]

# for post in posts:
#     print(post)

def summer(num_1, num_2, num_3=10, *args, **kwargs):
    total = 0
    total += (num_1 + num_2 + num_3)
    print(args)
    for arg in args:
        total += arg
    print(kwargs)
    for kwarg in kwargs.values():
        total += kwarg
    return total

print(summer(5, 10, 15, 20, 25, 30, 35, 46, num_9=50, num_10=75))


# print(summer(5, 10, 15))

# Sets
# my_set = { 1, 2, 3, False, "Whats up?"}
# my_list = [1, 2, 2, 3, 3, 4, 5 ]
# my_tuple = ("orange", "red", "red", "blue", "blue", "green" )

# my_set = set(my_list)
# print(list(my_set))
# print(my_set)
# my_set2 = set(my_tuple)
# print(tuple(my_set2))

# EMPTY SET
# new_set = set()


# new_set.add(2)
# new_set.add(3)
# print(new_set)
# print(1 in new_set)
# print(2 in new_set)

# new_set.discard(3)
# new_set.remove(2)
# print(new_set)

# other_set = {1, 1, 1, 2, 2, 2, 4}
# print(other_set)

# for color in my_tuple:
#     print(color)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}



# UNION\
# print(set_a | set_b)
# print(set_a.union(set_b))

# INTERSECTION
# print( set_a & set_b)
# print( set_a.intersection(set_b))

# DIFFERENCE
# print(set_a - set_b)
# print(set_b - set_a)
# print(set_a.difference(set_b))

# SYMMETRIC DIFFERENCE
# print(set_a ^ set_b)
# print(set_a.symmetric_difference(set_b))

# SPLAT *

# my_list = [2, 3, 4, 5]
# my_list2 = [*my_list]
# my_list2 = my_list
# print(my_list2)
# my_dict = {
#     "breakfast": "eggs",
#     "lunch": "salad"
# }

# my_dict2 = {**my_dict}
# print(my_dict2)

# FILTER, MAP, & lambdas

# FILTER
scores = [90, 87, 92, 95, 76, 69, 84, 90]

def a_grades(grade):
    return grade >= 90

higher_grades = filter(a_grades, scores)
higher_grades = filter(lambda grade: grade >= 90, scores)

print(higher_grades)
print(list(higher_grades))

for grade in set(higher_grades):
    pass


# names = ["JAMES", "julie", "Ana", "Ria"]
# # sorted_names = sorted(names, reverse=True)
# def case_maker(val):
#     return val.upper()


# sorted_names_og = sorted(names)
# sorted_names = sorted(names, key=lambda val: val.upper())
# print(sorted_names)


# MAPPING
def num_to_letter(num) -> str:
    """mapping function to change number grades to letter"""

    if num >= 90:
        return "A"
    elif num >= 80 and num < 90:
        return "B"
    elif num >= 70 and num < 80:
        return "C"
    elif num >= 60 and num < 70:
        return "D"
    else:
        return "F"

scores = [90, 87, 92, 95, 76, 69, 84, 90, 50]

mapped_scores = map(lambda val: val + 5,scores)
mapped_scores = map(num_to_letter, scores)

# print(mapped_scores)
# print(list(mapped_scores))

# nums = [ 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 

# What is the expected output of the following code? 

nums = set([1, 2, 2, 3, 3, 4, 4, 5]) 

# print(sum(nums)) 


# What is the expected output of the following code? 

nums = 1,2,3,4,5 

# print(sum(nums)) 

# Which of the following choices will print the “vals” list in reversed order?? 

vals = [ 5, 4, 3, 2, 1] 

# What data type will the following code print to the terminal? 

my_list = [1, 2, 3, 4, 5 ] 

# print(my_list[1:4]) 