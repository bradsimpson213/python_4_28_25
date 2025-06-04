
# from datetime import datetime

# start = datetime.now()
# print("start", start)

# count = 0

# for num in range(1_000_000_000):
#     count += 1

# end = datetime.now()
# print("COUNT", count)
# print("TIME IT TOOK", end - start)



# list_1 = []
# print(list_1[0])

# list_2 = [
#     [1, 2, 3], 
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(list_1[0][1])

# list_3 = [
#     [[1, 2, 4],[],[]], 
#     [[],[],[]],
#     [[],[],[]]
# ]
# print(list_1[0][0][1])


# NUMPY
import numpy as np
# list_sample = [1, 2, 3, 4, 5]
# print(list_sample)
# arr_1 = np.array(list_sample)
# print(arr_1)

list_2d = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

# print(list_2d)
# arr_2 = np.array(list_2d)
# print(arr_2[0, 1])
# list_2[0][1]

# arr_3 = np.arange(0, 11, 1)
# print(arr_3)
# print(arr_3[3])
# print(arr_3[1:4])

# TIC-TAC_TOE
# board = [
#     ["-", "-", "-"],
#     ["-", "-", "-"],
#     ["-", "-", "-"],
# ]

# np_board = np.array(board)

# np_board[1, 1] = "X"
# print(np_board)
# np_board[0, 2] = "O"
# print(np_board)
# np_board[1, 0] = "X"
# print(np_board)
# np_board[1,2] = "O"
# print(np_board)
# np_board[2,2] = "X"
# print(np_board)
# np_board[0,0] = "O"
# print(np_board)
# np_board[0,1] = "X"
# print(np_board)
# np_board[2,1] = "O"
# print(np_board)
# np_board[2,0] = "X"
# print(np_board)
# np_board[3,0] = "X"

# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8, 9, 10, 11, 12]
# print(list1 + list2)
# str1 = "Brad"
# str1 += " will most likely have pizza for lunch"
# print(str1)
# arr1 = np.array(list1)
# arr2 = np.array(list2)
# # print(arr1 + arr2)
# print(arr1 + 1)
# print(arr2 * 3)

# print(np.sum(arr2))
# print(np.min(arr2))
# print(np.max(arr2))
# print(len(arr2))

# import matplotlib.pyplot as plt

# from PIL import Image

# pic = Image.open("cats1.jpg")

# pic_arr = np.asarray(pic)

# print(pic_arr.shape)
# print(pic_arr)

# plt.imshow(pic_arr)
# plt.show()


# PANDAS

import pandas as pd


# data = {"foods": ["pizza", "hamburger", "salad"],
#         "calories": [800, 1000, 400]}

# df_1 = pd.DataFrame(data)
# print(df_1)

# cats = {'names': ["Blue", "Patch", "Mimi"],
#         "ages": [8, 8, 12],
#         "colors": ["Black", "Tuxedo", "Gray Tabby"]
# }

# cats_df = pd.DataFrame(cats)
# print(cats_df)

# df_states = pd.read_csv("states.csv", names=["State Name", "Abbrev", "State Code"], header=0)
# print(df_states)


df_netflix = pd.read_csv('netflix_titles.csv', sep="|", index_col=0)
print(df_netflix)