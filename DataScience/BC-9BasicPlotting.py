# Creating a Scatter Plot

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.rand(20,5),
columns= ['Jan','Feb', 'March','April', 'May'])
df.plot.scatter(x='Feb', y='Jan', title='Temperature over two months ')

#plt commands
plt.legend(bbox_to_anchor=(0.9, 0.5))  
plt.show()
