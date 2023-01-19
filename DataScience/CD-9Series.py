# Using a Series Name Attribute
std = pd.Series([77,89,65,90], name='StudentsMarks')
print (std.name)
# std = std.rename("Marks")
print (std.name)
# StudentsMarks
# Marks