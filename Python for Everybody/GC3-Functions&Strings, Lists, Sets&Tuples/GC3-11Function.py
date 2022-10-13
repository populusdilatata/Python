#Problem You need to unpack N elements from an iterable, 
#but the iterable may be longer than N elements, causing 
#a 'too many values to unpack' exception.
#1.2

items =[1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)
print(tail)

def sum(items):
    head, *tail = items
    return head+sum(tail) if tail else head
    
print(sum(items))
