#Problem: You want to define a function or method where one or more 
#of the arguments are optional and have a default value.
#7.5.1

def spam(a, b=42):
    print(a,b)
    
#Sample usage
spam(1)             # OK, a=1, b=42
spam(1,2)          # OK, a=1, b=2