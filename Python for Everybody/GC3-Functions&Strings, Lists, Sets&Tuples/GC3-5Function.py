#Problem: You want to return multiple values from a function.
#7.4

def myfun():
    return 1, 2, 3
    
#Sample usage
a, b, c = myfun()
print(a)
print(b)
print(c)
x=myfun()
print(x)