#Problem You want to keep a limited history of the last few items 
#seen during iteration or during some other kind of processing. 
#1.3

from collections import deque

def search(lines, pattern, history=5):
    previous_lines=deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)
        
#Example use an a file
if __name__ == '__main__':
    with open('something.txt') as f:
        for line, prevlines in search(f, 'python', 2):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)
            
#Sample usage
q= deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)                 #deque([1, 2, 3], maxlen=3)
q.append(4)
print(q)                 #deque([2, 3, 4], maxlen=3)
q.append(5)
print(q)                 #deque([3, 4, 5], maxlen=3)

