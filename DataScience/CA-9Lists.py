# convert string to a list of characters
Word = 'Egypt'
List1 = list(Word)
print (List1)
#['E', 'g', 'y', 'p', 't']

# use the delimiter
Greeting= 'Welcome-to-Egypt'
List2 =Greeting.split("-")
print (List2)
# #['Welcome', 'to', 'Egypt']
delimiter='-'
List2 =Greeting.split(delimiter)
print (List2)
#['Welcome', 'to', 'Egypt']
# we can break a string into words using the split method
Greeting= 'Welcome to Egypt'
List2 =Greeting.split()
print (List2)
# ['Welcome', 'to', 'Egypt']
print (List2[2])
# Egypt