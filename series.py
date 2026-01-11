import pandas as pd
import numpy as np

# se=pd.Series(['Rakesh','Hemlata','Kajal','Himanshu','Prashant'],index=[1, 2, 3, 4, 5])      #creates a series with custom index
# print("Original Series:\n",se)

# a=pd.read_csv("D:\Python Programs\libraries\pandas\Bsc.csv")   #reads dataframe from csv file
# ab=pd.Series(a['Name'])                                        #converts a dataframe column to series
# print("Series from DataFrame column 'name':\n",ab)
# print(ab)
# print(type(ab))                                                 #prints type of ab

newse=pd.DataFrame(np.random.rand(50,5), index=range(50))                          #creates a Dataframe with random numbers
# print("Series with random numbers:\n",newse)

# print(type(newse))                                             #prints type of newse
                                     
# newse.to_csv("outputwithindex.csv", index=True)                                  #saves dataframe to csv file

# print(newse.T)                                                   #transposes the dataframe

# print(newse.sort_index(axis=1, ascending=False))                #sorts dataframe columns in descending order

print(newse.sort_index(axis=0, ascending=False))                #sorts dataframe rows in descending order