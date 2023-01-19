# Adding and Updating List Elements

courses=["OOP","Networking","MIS","Project"]
students=["Bohdana", "Alice",
"Ctirad", "Drahoslav", "Doubravka"] 
OOP_marks = [65, 85, 92]
OOP_marks.append(50) # Add new element
OOP_marks.append(77) # Add new element
print (OOP_marks[ : ]) # Print list before updating
# [65, 85, 92, 50, 77]

OOP_marks[0]=70 # update new element
OOP_marks[1]=45 # update new element
list1 = [88, 93]
OOP_marks.extend(list1) # extend list with another list
print(OOP_marks[ : ]) # Print list after updating
# [70, 45, 92, 50, 77, 88, 93]