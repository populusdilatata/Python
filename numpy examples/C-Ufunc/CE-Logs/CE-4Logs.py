#NumPy does not provide any function to take log at any base, 
#so we can use the frompyfunc() function along 
#with inbuilt function math.log() with two input parameters 
#and one output parameter:

from math import log
import numpy as np

nplog = np.frompyfunc(log, 2, 1)

print(nplog(100, 15))