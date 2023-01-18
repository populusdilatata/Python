# Creating a Box Plot

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.rand(20,5),
columns=['Jan','Feb','March','April', 'May'])
df.plot.box()

#plt commands
plt.legend(bbox_to_anchor=(1.2, 1))  
plt.show()