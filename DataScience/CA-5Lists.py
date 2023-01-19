# List Operations
print (len([5, "Otmar", 3])) # find the list length.
# 3
print ([3, 4, 1] + ["Otmar", 5, 6]) # concatenate lists.
# [3, 4, 1, 'Otmar', 5, 6]
print (['CZ!'] * 4) # repeat an element in a list.
# ['CZ!', 'CZ!', 'CZ!', 'CZ!']
print (3 in [1, 2, 3]) # check if element in a list
# True
for x in [1, 2, 3]:
    print (x, end=' ') # traverse list elements
# 1 2 3