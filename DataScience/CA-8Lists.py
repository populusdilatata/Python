#List sorting and Traversing
seq=(41, 12, 9, 74, 3, 15) # use sequence for creating a list
tickets=list(seq)
print(tickets)
# [41, 12, 9, 74, 3, 15]
tickets.sort()
print(tickets)
#[3, 9, 12, 15, 41, 74]
print("\nSorted list elements ")
for ticket in tickets:
    print(ticket)

#Sorted list elements
#3
#9
#12
#15
#41
#74