
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
# board[0][0]
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
# df_netflix = pd.read_csv('netflix_titles.csv', sep="|", index_col=0)
# print(df_netflix)

# df_states = pd.read_csv("states.csv", names=["State Name", "Abbrev", "State Code"], header=0)
# print(df_states)

# print(df_states["State Name"])
# # print(df_states.loc[0])
# # print(df_states.loc[1:10])
# print(df_states.iloc[:10, 0:2])

# GROUPING
df_countries = pd.read_csv("countries.csv")
# print(df_countries)
# # print(df_countries)
# df_grouped = df_countries.groupby("Region")
# print(df_grouped["Population"].sum())


# data2 = {'A': [1, 2, 3, 4, 5], 'B': ["foo", "bar", "baz", "bar", "foo"]}
# df_grouping = pd.DataFrame(data2)
# print(df_grouping)
# grouped = df_grouping.groupby("B")
# print(grouped["A"].sum())

# df_pop_by_state = pd.read_csv("us_pop_by_state.csv")
# print(df_pop_by_state.head(10))
# print(df_pop_by_state.tail())
# print(df_pop_by_state.info())
# print(df_pop_by_state.columns)
# print(df_pop_by_state.size)
# print(df_pop_by_state.shape)
# print(df_pop_by_state.dtypes)
# print(df_pop_by_state)
# sorted_states = df_pop_by_state.sort_values("2020_census", ascending=False)
# print(sorted_states)

# df_houses= pd.read_csv("house_data.csv")
# print(df_houses)
# sorted_houses = df_houses.sort_values(["bedrooms", 'bathrooms'], ascending=False)
# print(sorted_houses.head(20))

# print(df_pop_by_state.info())
# print(df_pop_by_state[df_pop_by_state["percent_of_total"] >= .05])
# print(df_pop_by_state[df_pop_by_state["2020_census"].between(10_000_000, 20_000_000)])

# print(df_pop_by_state[df_pop_by_state["percent_of_total"].isna()])
# print(df_pop_by_state[df_pop_by_state["state_code"].isin(['PA', "NY", "NJ"])])

# list1 = [1, 2, 3]
# print(1 in list1)

# df_pop_by_state = pd.read_csv("us_pop_by_state.csv")
# df_states = pd.read_csv("states.csv", names=["State Name", "Abbrev", "state_code"], header=0)

# # print(df_pop_by_state.head())
# # print(df_states.head())
# merged_states = pd.merge(df_states, df_pop_by_state, on="state_code")
# print(merged_states)

# merged_states.drop(columns="state", inplace=True)
# merged_states.rename(columns={ "state_code": "State", "2020_census": "Population", "rank": "Rank", "percent_of_total": "%"}, inplace=True)
# # print(merged_states.head())

# merged_states["State Animal"] = "Cat"

# # print(merged_states.head())
# merged_states.insert(5, "State Flag", "Flag")
# print(merged_states.head())

# df_houses= pd.read_csv("house_data.csv")
# print(df_houses.head())
# df_houses["Total Rooms"] = df_houses['bedrooms'] + df_houses["bathrooms"]
# print(df_houses.head())

# print(df_houses[["bedrooms", 'bathrooms', 'Total Rooms']].sum())
# print(df_houses.max())
# print(df_houses.count())
# print(df_houses.describe())

# Matplotlib

import matplotlib.pyplot as plt

# print(plt.style.available)
# plt.figure(figsize=(10,5))
plt.style.use("dark_background")
# plt.plot(
#     [1, 2, 3, 4, 5], 
#     [2, 4, 6, 8, 10], 
#     color='blue', 
#     linewidth=2, 
#     linestyle="--",
#     label="Regular Learning"
# )
# plt.plot(
#     [1, 2, 3, 4, 5], 
#     [4, 8, 12, 16, 20], 
#     color='orange', 
#     linewidth=3, 
#     label="Game Coding"
# )
# plt.title("Brads Fun Graph")
# plt.xlabel("Hours")
# plt.ylabel("Fun Had")
# plt.legend()
# plt.xticks([1, 2, 3, 4, 5])
# plt.yticks([6, 12], labels=['6K', '12K'])
# plt.show()

# Bar Plots
# foods = ["Pizza", "Burgers", "Wings", 'Salad']
# times_cooked = [45, 67, 24, 13]
# times_ruinbed = [3, 6, 1, 3]
# # plt.bar(foods, times_cooked, color="green", label="Made Delicious")
# # plt.bar(foods, times_ruinbed, color="red", label="Made Yucky", bottom=times_cooked)
# plt.barh(foods, times_cooked, color="green", label="Made Delicious")
# plt.barh(foods, times_ruinbed, color="red", label="Made Yucky", left=times_cooked)
# plt.xlabel('Meals') 
# plt.ylabel('Time prepared') 
# plt.title('Foods Prepared') 
# plt.legend()
# plt.show()

# Histograms
# test_scores = [ 66, 77, 78, 78, 88, 91, 77, 78, 95, 78, 85, 81, 61, 78, 77, 68, 81, 83, 74]
# plt.hist(test_scores, bins=15)
# plt.title('Distribution of Test Scores')
# plt.show()

# Scatter PLot
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 8]
# plt.title("Cogs vs Sprockets")
# plt.scatter(x, x, marker="p", color="red", label="cogs")
# plt.scatter(x, y, marker="D", color="blue", label="sprockets")
# plt.legend()
# plt.show()

# Pie Charts
# labels = ["Building Improvements", "Deferred Maintenance", "Contractor Fees", "Taxes", "Site Improvements" ]
# costs = [47_945_970, 3_752_581, 7_340_612, 3_233_392, 18_345_789]
# colors = ["Blue", "red", 'green', "purple", "orange"]
# plt.title("Property Costs")
# plt.pie(costs, labels=labels, autopct="%1.2f%%", colors=colors, explode=(0, 0, 0.2, 0, 0.3) )
# plt.show()

# Box plots
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
# data_2 = [
#     [2, 4, 6, 8, 10, 12, 14],
#     [1, 4, 4, 5, 5, 6, 6, 7, 7, 8, 12],
#     [1, 2, 2, 3, 3, 7],
# ]
# plt.boxplot(data_2)
# plt.title("Box Plot Data")
# plt.show()


# Figures and Subplots, oh my!
plt.figure(figsize=(15, 4))
plt.suptitle("Brad's Many Charts")

plt.subplot(1,3,1)
foods = ["Pizza", "Burgers", "Wings", 'Salad']
times_cooked = [45, 67, 24, 13]
times_ruinbed = [3, 6, 1, 3]
plt.bar(foods, times_cooked, color="green", label="Made Delicious")
plt.bar(foods, times_ruinbed, color="red", label="Made Yucky", bottom=times_cooked)
plt.xlabel('Meals') 
plt.ylabel('Time prepared') 
plt.title('Foods Prepared') 
plt.legend()

plt.subplot(1,3,2)
plt.plot(
    [1, 2, 3, 4, 5], 
    [2, 4, 6, 8, 10], 
    color='blue', 
    linewidth=2, 
    linestyle="--",
    label="Regular Learning"
)
plt.plot(
    [1, 2, 3, 4, 5], 
    [4, 8, 12, 16, 20], 
    color='orange', 
    linewidth=3, 
    label="Game Coding"
)
plt.title("Brads Fun Graph")
plt.xlabel("Hours")
plt.ylabel("Fun Had")
plt.legend()
plt.xticks([1, 2, 3, 4, 5])
plt.yticks([6, 12], labels=['6K', '12K'])

plt.subplot(1, 3, 3)
labels = ["Building Improvements", "Deferred Maintenance", "Contractor Fees", "Taxes", "Site Improvements" ]
costs = [47_945_970, 3_752_581, 7_340_612, 3_233_392, 18_345_789]
colors = ["Blue", "red", 'green', "purple", "orange"]
plt.title("Property Costs")
plt.pie(costs, labels=labels, autopct="%1.2f%%", colors=colors, explode=(0, 0, 0.2, 0, 0) )
plt.show()


