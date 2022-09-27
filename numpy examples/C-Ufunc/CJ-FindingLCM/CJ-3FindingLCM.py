#Find the LCM of all values of an array where the array contains
#all integers from 1 to 10:
import numpy as np

arr = np.arange(1, 11)

x = np.lcm.reduce(arr)

print(x)