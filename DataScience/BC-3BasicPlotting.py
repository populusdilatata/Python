# Create a stacked bar plot

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.rand(20,5), columns=['Jan','Feb', 'March','April', 'May']) 
df.plot.bar(stacked=True, figsize=(20, 10))

#plt commands
plt.legend(bbox_to_anchor=(1.1, 1))  
plt.show()