#Use an if statement to check if the function is a ufunc or not:
import numpy as np

if type(np.add) == np.ufunc:
  print('add is ufunc')
else:
  print('add is not ufunc')