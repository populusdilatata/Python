#The around() function increments preceding digit or decimal by 1 if >=5 
#else do nothing.

#E.g. round off to 1 decimal point, 3.16666 is 3.2
import numpy as np

arr = np.around(3.1666, 2)

print(arr)