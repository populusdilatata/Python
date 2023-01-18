# A Pandas Data Frame
# Creating a Data Frame Using the Pandas Library

import pandas as pd
data =[['Lukas', 35], ['Ludvik', 17], ['Libor', 25]]
DataFrame1 = pd.DataFrame(data, columns=['Name','Age'])
print(DataFrame1)