# A Pandas Series 
# Create series from array using pandas and numpy
import pandas as pd
import numpy as np
data = np.array([90, 75, 50, 66])
s = pd.Series(data, index=['A', 'B', 'C', 'D'])
print(s)