# Example of Data Visualization

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

salesMen = ['Bohdana', 'Pravoslav', 'Alice', 'Edita', 'Radovan', 'Ctirad']
Mobile_Sales = [2540, 1370, 1320, 2000, 2100, 2150]
TV_Sales = [2200, 1900, 2150, 1850, 1770, 2000]
df = pd.DataFrame()
df ['Name'] =salesMen
df ['Mobile_Sales'] = Mobile_Sales
df['TV_Sales']=TV_Sales
df.set_index("Name",drop=True,inplace=True)

print(df)

# Create a bar plot of the sales volume

df.plot.bar( figsize=(20, 10), rot=0)
plt.legend(bbox_to_anchor=(1.1, 1)) 
plt.xlabel('Salesmen') 
plt.ylabel('Sales')
plt.title('Sales Volume for salesmen in \nJanuary and April 2017')
plt.show()

# Create a pie chart of item sales.
                                                              
df.plot.pie(subplots=True)
plt.show()
# Create a box plot of item sales.

df.plot.box()
plt.show()

# Create an area plot of item sales.

df.plot.area(figsize=(6, 4))
plt.legend(bbox_to_anchor=(1.3,1))
plt.show()

# Create a stacked bar plot of item sales.

df.plot.bar(stacked=True, figsize=(20, 10))
plt.legend(bbox_to_anchor=(1.1, 1))
plt.show()