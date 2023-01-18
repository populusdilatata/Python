# Pandas Calculations 
import pandas as pd
d = {
'Name': pd.Series(['Alice','Bob','Charlie','David','Edward',
'Fred','Gabriel','Horace','Ivan','Juliet',
'Kylian','Lukas']),
'Age': pd.Series([34,26,25,27,30,54,23,43,40,30,28,46]),
'Height':pd.Series([114.23,173.24,153.98,172.0,153.20,164.6,
183.8,163.78,172.0,164.8 ])}
df = pd.DataFrame(d) #Create a DataFrame
print(df.std())# Calculate and print the standard deviation
print(df.describe())
print ("Mean Values in the Distribution")
print (df.mean())
print ("*******************************")
print ("Median Values in the Distribution")
print (df.median())
print ("*******************************")
print ("Mode Values in the Distribution")
print (df['Height'].mode())