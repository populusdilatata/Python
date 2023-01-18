# A Pandas Series
# Create series from dictionary using pandas
import pandas as pd
import numpy as np
data = {'Lukas': 92, 'Libor': 55, 'Ludvik': 83}
s = pd.Series(data, index=['Lukas', 'Libor', 'Ludvik'])
print(s)