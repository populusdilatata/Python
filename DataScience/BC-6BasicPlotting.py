# Multiple Histograms per Column

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

df=pd.DataFrame({'April':np.random.randn(1000)+1,
'May':np.random.randn(1000),
'June': np.random.randn(1000) - 1}, 
columns=['April', 'May', 'June'])
df.hist(bins=20)

#plt commands
plt.legend(bbox_to_anchor=(1.2, 1))  
plt.show()