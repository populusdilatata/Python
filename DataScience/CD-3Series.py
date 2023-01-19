# Slicing Data from a Series
import numpy as np
import pandas as pd

Series1 = pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd'])
print(Series1)
#a 0.350241
#b -1.214802
#c 0.704124
#
#dtype: float64

print(Series1.index)
#Index(['a', 'b', 'c', 'd'], dtype='object')

print (" \n Series slicing ")
print (Series1[:3])
# Series slicing
# a 0.350241
# b -1.214802
# c 0.704124
# dtype: float64
print ("\nIndex accessing")
print (Series1[[3,1,0]])
# Index accessing
# d 0.866934
# b -1.214802
# a 0.350241
# dtype: float64
print ("\nSingle index")
x = Series1[0]
print (x)

# Single index
# 0.35024081401881596
