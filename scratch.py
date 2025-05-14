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
while True:
    print(f"{i}. Hello, world.")
    if index < 4:
        index += 1
        continue
    print("You've printed 5 times. Goodbye.")
    if index > 5:
        break


# lunches = ["hamburger", 'salad', "wings"]
# for lunch in lunches:
#     print(lunch)
#     print(lunch.upper())



lunches = [1, 2, 3, 4, 5]
# picked_value = random.choice(lunches)
for lunch in lunches:
    print(lunch + 1)

print(2 in lunches)
print(212 in lunches)

print("h" in "hello")
print("H" in "hello")