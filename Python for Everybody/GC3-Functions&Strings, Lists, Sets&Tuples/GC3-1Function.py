#Problem: You want to write a function that accepts any number of input arguments
#Chapter 7.1

def avg(first, *rest):
    return (first +sum(rest))/(1+len(rest))

#Sample use
print(avg(1,2))
print(avg(1,2,3,4))
