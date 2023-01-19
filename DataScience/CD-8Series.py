# Vectorizing Operations on a Series
SerX = pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])
print ("Addition");
print( SerX + SerX)
print ("Addition with non-matched labels");
print (SerX[1:] + SerX[:-1])
print ("Multiplication");
print (SerX * SerX)
print ("Exponential");
print (np.exp(SerX))

# Addition
# a 2
# b 4
# c 6
# d 8
# dtype: int64
# Addition with non-matched labels
# a NaN
# b 4.0
# c 6.0
# d NaN
# dtype: float64
# Multiplication
# a 1
# b 4
# c 9
# d 16
# dtype: int64
# Exponential
# a 2.718282
# b 7.389056
# c 20.085537
# d 54.598150
# dtype: float64