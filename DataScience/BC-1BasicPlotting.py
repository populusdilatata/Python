# Running Basic Plotting

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


df = pd.DataFrame(np.random.randn(200,6),index= pd.date_range('1/9/2009', periods=200), columns= list('ABCDEF'))
df.plot(figsize=(20, 10))
plt.legend(bbox_to_anchor=(1, 1))
  
# show the plot
plt.show()