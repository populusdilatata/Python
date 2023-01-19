# Altering a Series and Using the Get() Method
print ("\nUse the get and set methods to access"
"a series values by index label\n")
SeriesDict2 = pd.Series(dict, index=['y', 'm', 'd', 's']) 
print (SeriesDict2['y']) # Display the year
SeriesDict2['y']=1999 # change the year value
print (SeriesDict2) # Display all dictionary values 
print (SeriesDict2.get('y')) # get specific value by its key
# Use the get and set methods to access a series values  by index label
# 2018
# y 1999
# m 2
# d Sunday
# s NaN
# dtype: object
# 1999