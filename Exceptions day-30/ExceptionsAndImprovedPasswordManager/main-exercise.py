# fruits = ["Apple", "Pear", "Orange"]
#
# #First *fork* your copy. Then copy-paste your code below this line 👇
# #Finally click "Run" to execute the tests
#
# #TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
# make_pie(4)


facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        # total_likes = total_likes + 0
        pass


print(total_likes)