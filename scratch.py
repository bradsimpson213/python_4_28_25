# # name = 'Brad'
# # print(name)

# # list_example = [1, 2, 3, 4, 5, [True, False]]



# # print(5)
# # print(5.23)
# # print(500_000_000_000_000)
# # print("Hello!")
# # print('Hi there!')
# # print("That's great!")
# # print('''This is now
# # a multiline string,
# # so many lines!''')
# # print(True)
# # print(False)
# # print(None)


# # Varaibles

# # big_num = 5_000_000_000_000_000
# # print(big_num)
# # big_num += 1_000_000_000_000
# # print(big_num)
# # big_num = 5
# # print(big_num)
# # big_num = "yes"
# # print(big_num)

# # text_1 = None
# # text_2 = "Brad"

# # num_1 = 5
# # num_1 += 5  # 5 + 5
# # print(num_1)

# # val_1 = 40
# # val_2 = "hello"
# # val_3 = 40
# # val_4 = True


# print(True == 1)
# print(False == 0)
# print(False is 0)
# print(True is 1)
# print(bin(True))
# print(bin(False))
# print(bin(1))
# print(bin(0))
# print(bin(100))

# # print("Hello!")
# # print("Hello!")
# # print("Hello!")
# # print("Hello!")

# # print(10 * 2)
# # num = 10
# # print(num)
# # num += 10
# # print(num)
# # num *= 2
# # num_1 = ( num + 7 - 10) * 3
# # PEMDASprint("hello")

# greeting = "Hello"

# my_list = ["sandwich", "pizza", "salad" ]

# MY_NAME = "Brad"
# PII = 3.14
# print(MY_NAME, PII)
# PII = 12
# print(PII)

# # Math

# # Division in python
# reg_div = 10 / 2
# int_div = 10 // 2
# print('Regular', reg_div)
# print('int', int_div)
# print(10 // 3 )
# print(10 % 3)
# print(10 % 2)
# print(11 % 2 == 0)
# print(5 * 5)
# print(5 ** 2)
# print(5 ** 5)

# # ==

# # STRINGS
# name = 'Brad'
# text = """
# This is a multi line string
# so it can span lots

# and lots of lines and 
# spaces and new lines are preserved
# """

# print(text)
# print(4)
# print(len(text))

# # Indexing
# name = 'Brad'
# #       0123
# # name[0:len(name)]
# # print(name[-1])
# # print(name[start:stop:step])
# # print(name[1:3])
# # print(name[2:])
# # print(name[:3:2])
# # print(name[::-1])

# # lunches = ["soup", "wings", "tacos"]
# # print(lunches[2][2])
# # print(lunches[:])

# # print(f"{name} thinks python is fun!")
# # name = "Nicole"
# # print(f"{name.upper()} thinks python is fun!")

# # turns = 5
# # print(f"you just took turn {turns}")

# # turns -= 1
# # print(f"you just took turn { 4 + 8 }")

# # def say_hi(name):
# #     print(f"Hello {name}!")


# # say_hi("Brad")
# # say_hi("Nicole")

# # text = "This is a h sentence"
# # print(text.find("h"))
# # print(text.rfind("h"))

# # import random 

# # random.randint()

# user_input = int(input("Please enter an integer: "))
# print(user_input + 10)

# print(float(4))
# print(int(3.45))
# print(str(2.34))
# print(int("4"))

# breakfast_choice = input("What are you having for breakfast?: ").lower()

# if breakfast_choice == 'waffles':
#     print("Waffles are amazing, great choice!")

# elif breakfast_choice == 'pancakes':
#     print("Pancakes are a good choice!")

# elif breakfast_choice == 'eggs':
#     print("I hope you didn't ned a loan to buy those eggs..")

# else:
#     print("Thats not my favorite...")

# # Looping
# index = 0
# while index < 20:
#   print("Hi")
#   index += 1
# else:
#   print("Yahoo!")


# index = 0
# while True:
#     print(f"{i}. Hello, world.")
#     if index < 4:
#         index += 1
#         continue
#     print("You've printed 5 times. Goodbye.")
#     if index > 5:
#         break


# lunches = ["hamburger", 'salad', "wings"]
# for lunch in lunches:
#     print(lunch)
#     print(lunch.upper())



# lunches = [1, 2, 3, 4, 5]
# # picked_value = random.choice(lunches)
# for lunch in lunches:
#     print(lunch + 1)

# print(2 in lunches)
# print(212 in lunches)

# print("h" in "hello")
# print("H" in "hello")


# print( 0 == False )
# print( 1 == True )
# print(bin(1))
# print(bin(True))

# my_tuple = 1, 2
# my_tuple2 = my_tuple + (2, 3)
# print(my_tuple2)

# x = [0, 1, 2]
# x.insert(0, 1)
# print(x)
# del x[1]
# print(x)
# print(sum(x))

# list1= [1, 3]
# list2 = list1
# list1[0] = 4
# print(list2)

# nums = [1, 2, 3]
# vals = nums
# del vals[1:2]

# print("VALS", vals)
# print("NUMS", nums)

# dct = {}
# dct['1'] = (1, 2)
# { "1": (1, 2)}
# dct["2"] = (2, 1)
# { "1": (1, 2), "2": (1, 2)}

# for x in dct.keys():
#     print(dct[x][1], end="")

# d = {}
# d[1] = 1
# d["1"] = 2
# d[1] += 1
# print(d)

# sum = 0

# for k in d.keys():
#     sum += d[k]

# print(sum)

# dictionary = {
#     "one": "two",
#     "three": "one",
#     "two": "three",
# }

# v = dictionary["one"]

# for k in range(len(dictionary)): 
#     temp = v
#     v = dictionary[v]
#     print("KEY", temp, "VAL", v)

# print(v)


# my_list = [3, 1, -1]
# my_list[-1] = my_list[-2]
# print(my_list)

# data = ((1, 2),) * 7
# print(data)
# print(len(data[3:8]))
# print(data[3:8])

# list1 = [[1, 2],] * 7
# print(list1)

# tup = 1, + 1, 
# print(tup)
# tup = tup + tup
# print(tup)

# data = (1, 2, 4, 8)
# data = data[-2:-1]
# print(data)
# data = data[-1]
# print(data)
# print(data)

# vals = (4,)

# print(f"({vals[0]})")

# my_list = [1, 2]

# for v in range(2): #[0,1]
#     my_list.insert(-1, my_list[v])
#     print(v, my_list[v], my_list)

# print(my_list)

# stack = [1, 2, 3, 4, 5]

# queue = [6, 7, 8, 9, 10]

# data = {"name": "Peter", "age": 30 }
# person = data.copy()
# print(id(person))
# print(id(data))
# print(id(data) == id(person))


# my_lst = [4, 1, 7, 2, "A"]
# # my_lst.reverse()
# # print(my_lst)
# reversed(my_lst)
# print(my_lst)

# data1 = "1", "2"
# data2 = ("3", '4')=====
# data3 = data1 + data2
# print(data3)

# data = (1, 2, 4, 8)
# data = data[1:-1]
# data = data[0]
# print(data)

# my_list = [3, 1, -2]
# print(my_list[-1])
# print(my_list[-2])

# w = [7, 3, 23, 42]
# x = w[1:]
# y = w[1:]
# z = w
# print(x, y, z)
# y[0] = 10
# z[1] = 20
# print(x, y, z)
# print(w)

# data = {"a": 1, "b": 2, "c": 3}
# # print(data["a", 'b'])
# print([data["a"], data["b"]])

# print(list(range(-1, -2)))
# L = [i for i in range(-1, -2)]
# print(L)

# my_list = [0, 1, 2, 3]
# x = 1
# for elem in my_list:
#     x *= elem
# print(x)

# nums = [1, 2, 3]
# data = ("Peter",) * (len(nums) - nums[::-1][0])

# print(nums[::-1])
# print(data)

# t1 = (1, 4, 9)
# t2 = ("A", 'D', 'Z')
# t3= (True, False, None)
# t4 = (5.0 ,7.5, 9.9)
# t1, t3 = t2, t4
# print(t1)

data = (1, ) * 3
print(data)
# data[0] = 2
# print(data)

# do # 39 next class