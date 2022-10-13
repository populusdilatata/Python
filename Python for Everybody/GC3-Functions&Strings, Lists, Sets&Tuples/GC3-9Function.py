#Problem You have a callable that you would like to use 
#with some other Python code, possibly as  a callback function or handler, 
#but it takes too many arguments and causes an exception  when called:
#7.8

def spam(a, b, c, d):
    print(a, b, c, d)
    
    
#Sample usage

from functools import partial
s1=partial(spam, 1)
print(s1)
s1(2, 3, 4)
print(s1)
s1(4, 5, 6)
s2=partial(spam, d=42)
print(s2)
s2(1, 2, 3)
print(s2)
s2(4, 5, 6)
print(s2)
s3=partial(spam,1, 2, d=42)
print(s3)
s3(3)
print(s3)
s3(4)
print(s3)
s3(5)
print(s3)
