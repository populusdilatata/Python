#Find the difference of the set1 from set2:
import numpy as np

set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr = np.setdiff1d(set1, set2, assume_unique=True)
#the setdiff1d() method takes an optional argument assume_unique, 
#which if set to True can speed up computation. 
#It should always be set to True when dealing with sets.
print(newarr)