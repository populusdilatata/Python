# Accessing Dictionary Elements
Staff_Salary = { 'Otmar ' : 30000 , 'Alice' :24000, 
'Ctirad': 25000, 'Drahoslav':10000}

print('Salary package for Ctirad is \n')
# access specific dictionary element
print(Staff_Salary['Ctirad'])
#Salary package for Ossama Hashim is 25000


# Define a function to return salary after discount tax  5% 
def Netsalary (salary):
    return salary - (salary * 0.05) # also, could be return salary *0.95
    
#Iterate all elements in a dictionary
print ("Name" , '\t', "Net Salary" )
for key, value in Staff_Salary.items():
    print (key , '\t', Netsalary(value))
    
#Name Net Salary
#Otmar  28500.0
#Alice 22800.0
#Ctirad 23750.0
#Drahoslav 9500.0