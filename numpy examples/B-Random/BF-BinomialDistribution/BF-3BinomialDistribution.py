#The main difference is that normal distribution is continous 
#whereas binomial is discrete, but if there are enough data points 
#it will be quite similar to normal distribution with certain loc and scale.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')

plt.show()