#Problem: You want to define a function or method where one or more 
#of the arguments are optional and have a default value.
#If the default value is supposed to be a mutuable container, such as a list,
#set, or dictionary use None as the default and write code like this:
#7.5.3

# If, instead of providing a default value, you want to write code 
# that merely tests whether an optional argument was given 
# an interesting value or not, use this idiom:

_no_value=object()

def spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')
      
    print(a,b)
    
#Sample usage
spam(1)            #  a=1, b= <object object at 0x000001E777F681C0> 
spam(1, 2)         #  a=1, b=2
spam(1, None)      #  a=1, b=None