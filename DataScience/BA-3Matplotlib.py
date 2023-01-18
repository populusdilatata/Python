# Importing and Using the Seaborn Library

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
plt.style.use("seaborn-v0_8")
# Create some data
data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]],
size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])
# Plot the data with seaborn
sns.distplot(data['x'])
sns.distplot(data['y']);
# Plot 1
plt.show()
