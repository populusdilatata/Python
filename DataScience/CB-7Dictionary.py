# Sorting a Dictionary
Staff_Salary = { 'Otmar' : 30000 , 'Alice' : 24000, 
'Bob': 25000, 'Majka':10000}
print ("\nSorted by key")
for k in sorted(Staff_Salary):
    print (k, Staff_Salary[k])
#Sorted by key
# Alice 24000
# Bob 25000
# Majka 10000
# Otmar 30000
Staff_Salary = { 'Otmar' : 30000 , 'Alice' : 24000, 
'Bob': 25000, 'Majka':10000}
print ("\nSorted by value")
for w in sorted(Staff_Salary, key=Staff_Salary.get, reverse=True):
    print (w, Staff_Salary[w])

#Sorted by value
Otmar 30000
Bob 25000
Alice 24000
Majka 10000