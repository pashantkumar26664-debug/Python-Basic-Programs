import pandas as pd
import numpy as np

new=pd.read_csv("D:\Python Programs\libraries\pandas\example_file.csv")                        #reads dataframe from csv file
# print(new.head(20))                                                #prints first 20 rows
# print(new.tail(10))                 

# print(new['Notes'][0])                               #prints first row of 'Notes' column

new['Notes'][0]="This is modified note"               #modifies first row of 'Notes' column
# print(new['Notes'][0])                               #prints first row of 'Notes' column after modification

new.to_csv("example_file.csv", index=False)          #saves modified dataframe to existing file