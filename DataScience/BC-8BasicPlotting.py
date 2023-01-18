# Creating an Area Plot

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.rand(20,5),
columns= ['Jan','Feb','March','April', 'May'])
df.plot.area(figsize=(6, 6))

#plt commands
plt.legend(bbox_to_anchor=(0.9, 0.5))  
plt.show()

