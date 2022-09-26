#Draw out a sample for rayleigh distribution with scale of 2 with size 2x3:S
from numpy import random

x = random.rayleigh(scale=2, size=(2, 3))

print(x)