# A Pandas Data Frame
# Creating a Data Frame Using the Pandas Library and dictionary

import pandas as pd
data = {'Name':['Lukas', 'Libor', 'Ludvik',
'Leopold'],'Age':[35,17,25,30]}
dataframe2 = pd.DataFrame(data, index=[100, 101, 102, 103])
print (dataframe2)