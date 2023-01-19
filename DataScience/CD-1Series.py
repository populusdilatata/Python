# Creating a Series of Ndarray Data with Labels

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