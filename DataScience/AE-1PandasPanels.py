# A Pandas Data Frame
# Creating a Panel Using the Pandas Library
# Creating a panel

import pandas as pd
import numpy as np
data = {'Temperature Day1' : pd.DataFrame(np.random.
randn(4, 3)),'Temperature Day2' : pd.DataFrame
(np.random.randn(4, 2))}
p = pd.Panel(data)
print (p['Temperature Day1'])