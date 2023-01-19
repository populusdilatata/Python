# Implementing Dictionary Methods
Staff_Salary = { 'Otmar' : 30000 , 'Alice' : 24000, 'Edita': 25000, 
'Ivana':10000}
STDMarks={ "Doubravka":50, "Drahoslav":80, "Pravoslav":90}
print (Staff_Salary.get('Alice'))
# 24000
print (STDMarks.items())
# dict_items([('Doubravka', 50), ('Drahoslav', 80), ('Pravoslav', 90)])
print (Staff_Salary.keys())
# dict_keys(['Otmar', 'Alice', 'Edita', 'Ivana'])
print()
STDMarks.setdefault('Alice')
print (STDMarks)
# {'Doubravka': 50, 'Drahoslav': 80, 'Pravoslav': 90, 'Alice': None}
print (STDMarks.update(Staff_Salary))
# None
print (STDMarks)
# {'Doubravka': 50, 'Drahoslav': 80, 'Pravoslav': 90, 
# 'Alice': 24000, 'Otmar': 30000, 'Edita': 25000, 'Ivana': 10000}
