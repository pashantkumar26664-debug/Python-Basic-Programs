import pandas as pd
import numpy as np

dict1={
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 40],
    "city": ["New York", "Los Angeles", "Chicago", "Houston"],
    "marks": [85, 90, 95, 80],
    "married": [False, True, False, True]
}
df=pd.DataFrame(dict1)
print("Original DataFrame:")
print(df)
# df.to_csv("first.csv", index=True)                              #saves dataframe to csv file
# df.to_excel("first.xlsx", index=True)                            #saves dataframe to excel file
# print(df.head(2))                                            #prints first 2 rows
# print(df.tail(2))                                            #prints last 2 rows

print(df.describe())                                                  #gives statistical summary of numerical columns

# df.loc[2, 'age'] = 36                                                #modifies value at row index 2 and column 'age'
# print("\nDataFrame after modifying age of index 2:")
# print(df)

# df.drop('city', axis=1, inplace=True)                             #drops the 'city' column
# print(df)

newdf= df.copy()                                                        #creates a copy of dataframe

# print(newdf.rename(columns={'marks': 'new_marks'}))                                      #prints the dataframe with renamed column 'marks' to 'new_marks'

# print(newdf.loc[[1,2], ['age']])                             #selects rows with index 1 and 2 for column 'age'           

# print(newdf.loc[(newdf['age'] > 30) & (newdf['marks'] > 85)])        #finds rows where age is greater than 30 and marks greater than 85

# print(newdf.iloc[[2],[0,2]])                                       #selects all rows for columns at index 0 and 2

print(newdf.drop([0]))                                           #drops row with index 0

print(newdf.sort_values(by='marks', ascending=False))              #sorts dataframe by 'marks' column in descending order

