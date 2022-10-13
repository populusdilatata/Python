#Problem: You want to write a function that accepts 
#certain arguments by keyword.
#Chapter 7.2.1

def recv(maxsize, *, block):
    print('Receives a message')
    pass
#Sample usage    
#recv(1024, True)  #TypeError
print(recv(1024, block=True))