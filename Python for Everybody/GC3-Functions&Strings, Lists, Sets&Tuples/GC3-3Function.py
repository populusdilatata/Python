#Problem: You want to write a function that accepts 
#certain arguments by keyword.
#Chapter 7.2.2

def minimum(*values, clip=None):
    m=min(values)
    if clip is not None:
      m=clip if clip >m else m
    return m
    
#Sample usage 
print(minimum(1, 5, 2, -5, 10))               #return -5
print(minimum(1, 5, 2, -5, 10, clip=0))       #return 0
    