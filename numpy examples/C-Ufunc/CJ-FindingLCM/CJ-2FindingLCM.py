#Find the LCM of the values of the following array:
import numpy as np

arr = np.array([3, 6, 9])

x = np.lcm.reduce(arr)

print(x)