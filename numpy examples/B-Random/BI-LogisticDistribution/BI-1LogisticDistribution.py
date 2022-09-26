#Draw 2x3 samples from a logistic distribution with mean at 1 and stddev 2.0:
from numpy import random

x = random.logistic(loc=1, scale=2, size=(2, 3))

print(x)