# Creating a Series of Ndarray Data Without Labels
import numpy as np
import pandas as pd
Series2 = pd.Series(np.random.randn(4))
print(Series2)
# 0 1.784219
# 1 -0.627832
# 2 0.429453
# 3 -0.473971
# dtype: float64
print(Series2.index)
# RangeIndex(start=0, stop=4, step=1)