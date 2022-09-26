#Draw out a sample for pareto distribution with shape of 2 with size 2x3:
from numpy import random

x = random.pareto(a=2, size=(2, 3))

print(x)