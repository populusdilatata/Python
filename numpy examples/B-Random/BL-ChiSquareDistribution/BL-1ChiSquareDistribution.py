#Draw out a sample for chi squared distribution with 
#degree of freedom 2 with size 2x3:
from numpy import random

x = random.chisquare(df=2, size=(2, 3))

print(x)