# Sample Operations in a Series

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
# Index(['a', 'b', 'c', 'd'], dtype='object')
print ("\nSeries Sample operations")
print ("\n Series values greater than the mean: %.4f"
# Series1.mean())
print (Series1 [Series1> Series1.mean()])
print ("\n Series values greater than the
# Meadian:%.4f" % Series1.median())
print (Series1 [Series1> Series1.median()])
print ("\nExponential value ")
# Series1Exp = np.exp(Series1)
print (Series1Exp)
# Series Sample operations
# Series values greater than the mean: 0.1766
# a 0.350241
# c 0.704124
# d 0.866934
# dtype: float64
# Series values greater than the Median: 0.5272
# c 0.704124
# d 0.866934
# dtype: float64
# Exponential value
# a 1.419409
# b 0.296769
# c 2.022075
# d 2.379604
# dtype: float64