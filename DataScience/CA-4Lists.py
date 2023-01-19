# Deleting an Element from a List
OOP_marks = [70, 45, 92, 50, 77, 45]
print (OOP_marks)
# [70, 45, 92, 50, 77, 45]
del OOP_marks[0] # delete an element using del
print (OOP_marks)
# [45, 92, 50, 77, 45]
OOP_marks.remove (45) # remove an element using
remove() method
print (OOP_marks)
#[92, 50, 77, 45] 
OOP_marks.pop (2) # remove an element using pop()
method
print (OOP_marks)
# [92, 50, 45]