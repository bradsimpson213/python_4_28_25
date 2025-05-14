# Module 3 Structured Data

# Lists
my_list = [1, 2, 3, True, None, "Hello"]
my_list2 = []
# my_list3 = ['wings', 'pizza', 'salad', 'sandwich', "burger"]

# LIST INDEXING
# print(my_list3)
# print(my_list3[1])
# print(my_list3[-1])
# print(my_list3[1:2])
# print(my_list3[::2])
# print(my_list3[::-1])
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
foods = ['wing', 'pizza', 'salad', 'sandwich', "burger"]

# for food in foods:
#     print(food + "s")

# print("wing" in foods)
# print("donut" in foods)
print(list(range(len(foods))))

# for index in range(len(foods)):
#     print(f"{index + 1}. {foods[index]}")
#     if index > 0:
#         print(f"{foods[index -1]} is not the same as {foods[index]}")


index = 1
while index < len(foods):
    print(f"{index + 1}. {foods[index]}")
    if index > 0:
        print(f"{foods[index -1]} is not the same as {foods[index]}")
    index += 1


# image_data = [
#     [[25, 50, 75],
#      [25, 50, 75],
#      [50, 75, 100]],
#     [[30, 35, 250],
#      [],
#      []],
#     [[40, 45, 90],
#      [],
#      []],
# ]
# print(image_data[0][0][0])


# Tuples
my_tuple = (1, 2, 3, False, "Bye")
my_other_tuple = 2, 3, 4, 5
print(my_other_tuple)

empty_tuple = ()
single_val_tuple = 1,  # or (1, )

tup = ("red", "blue")
tup = ("yellow", "green")  # no error, this works
print(tup)                 # ("yellow", "green")
tup += tup + ("red", "blue")    # no error, this works
print(tup)    


print(tup[1:3])

for color in tup:
    print(color)

sorted_colors = sorted(tup)
print(tuple(sorted_colors))

# Dictionary
# my_dict = {
#     "name": 'Brad',
#     "age": "old",
#     4: "the number 4"
# }

# my_other_dict = {"name": "Brad", "age": 47}

# my_table = [
#     {"sales": 10, "date": "Monday"},
#     {"sales": 15, "date": "Tuesday"}
# ]


# Sets
# my_set = { 1, 2, 3, False, "Whats up?"}