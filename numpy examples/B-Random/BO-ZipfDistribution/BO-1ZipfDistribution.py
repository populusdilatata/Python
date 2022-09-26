#Draw out a sample for zipf distribution 
#with distribution parameter 2 with size 2x3:
from numpy import random

x = random.zipf(a=2, size=(2, 3))

print(x)