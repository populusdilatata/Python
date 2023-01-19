import operator
MarksCIS = [(88,65),(70,90,85), (55,88,44)]
print (MarksCIS) # original tuples
# [(88, 65), (70, 90, 85), (55, 88, 44)]
print (sorted(MarksCIS)) # direct sorting
# [(55, 88, 44), (70, 90, 85), (88, 65)]
print (MarksCIS) # original tuples
# [(88, 65), (70, 90, 85), (55, 88, 44)]
#create a new sorted tuple
MarksCIS2 = sorted(MarksCIS, key=lambda x: (x[0], x[1]))
print (MarksCIS2)
# [(55, 88, 44), (70, 90, 85), (88, 65)]
print (MarksCIS) # original tuples
# [(88, 65), (70, 90, 85), (55, 88, 44)]
MarksCIS.sort(key=lambda x: (x[0], x[1])) # sort in tuple
print (MarksCIS)
# [(55, 88, 44), (70, 90, 85), (88, 65)]