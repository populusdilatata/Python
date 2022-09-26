#Generate a random 1x10 array of Poisson distribution for occurence 2:
from numpy import random

x = random.poisson(lam=2, size=10)

print(x)