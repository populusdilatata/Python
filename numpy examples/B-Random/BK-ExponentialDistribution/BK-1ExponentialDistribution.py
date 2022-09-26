#Exponential Distribution
#Draw out a sample for exponential distribution with 2.0 scale with 2x3 size:
from numpy import random

x = random.exponential(scale=2, size=(2, 3))

print(x)