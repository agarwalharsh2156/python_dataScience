# import the necessary library i.e. pandas for using its methods
import pandas as pd
import numpy as np

# pass a dictionary object in the .DataFrame() to convert it into a data frame
dictionary = {"Gender": ["Male", "Female"], "Age": [21, 20], "Occupation": ["IT student", "Python_Enthusiast"]}
df = pd.DataFrame(dictionary , index=["Cindy", "Chinki"])
print(df,"\n")

# using an attribute with the object dataframe created and passing the index for the value we want to retrieve
# attribute can simply be assumed as the column name
# this technique returns a cell in a particular attribute at a particular row index
print(df.Age["Chinki"],"\n")

# Series : Each column of a dataFrame is known as Series
# You can access a column(Series) using the code example shown below
print(df["Occupation"],"\n")

# .max() can be used over a particular series to know the maximum among the entries in the table
# .min() can be used to know the minimum
print(df["Age"].max())
print(df["Age"].min(),"\n")

# .describe() outputs the basic statistical interpretation of the numeic data
print(df["Age"].describe(),"\n")

# .groupby() groups the data based on a particular series
print(df.groupby("Age")["Gender"].describe())