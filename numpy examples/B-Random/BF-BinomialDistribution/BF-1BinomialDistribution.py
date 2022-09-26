#Given 10 trials for coin toss generate 10 data points:
from numpy import random

x = random.binomial(n=10, p=0.5, size=10)

print(x)