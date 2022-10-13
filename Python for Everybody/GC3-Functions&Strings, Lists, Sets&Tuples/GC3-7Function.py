#Problem: You want to define a function or method where one or more 
#of the arguments are optional and have a default value.
#If the default value is supposed to be a mutuable container, such as a list,
#set, or dictionary use None as the default and write code like this:
#7.5.2

def spam(a, b=None):
    if b is None:
        b=[]
      
    print(a,b)
    
#Sample usage
spam(1)             # OK, a=1, b=[]
spam(1,2)          # OK, a=1, b=2
