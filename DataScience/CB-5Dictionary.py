# Implementing Dictionary Functions

Staff_Salary = { 'Otmar' : 30000 , 'Alice' : 24000, 'Ctirad': 25000,
'Drahoslav':10000}
STDMarks={ "Doubravka":50, "Edita":80, "Pravoslav":90}

def cmp(a, b):
    for key, value in a.items():
        for key1, value1 in b.items():
            return (key >key1) - (key < key1)
print (cmp(STDMarks,Staff_Salary))
# -1
print (cmp(STDMarks,STDMarks))
# 0
print (len(STDMarks))
# 3
print (str(STDMarks))
# {'Doubravka': 50, 'Edita': 80, 'Pravoslav': 90}
print (type(STDMarks))
# <class 'dict'>
