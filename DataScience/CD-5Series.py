# Creating a Series from a Dictionary
dict = {'m' : 2, 'y' : 2018, 'd' : 'Sunday'}
print ("\nSeries of non declared index")
# SeriesDict1 = pd.Series(dict)
print(SeriesDict1)
print ("\nSeries of declared index")
#SeriesDict2 = pd.Series(dict, index=['y', 'm', 'd',  's']) 
print(SeriesDict2)
#Series of non declared index
#d Sunday
# m 2
# y 2018
# dtype: object
# Series of declared index
# y 2018
# m 2
# d Sunday
# s NaN
# dtype: object