import numpy as np
import pandas as pd

data = {
    'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
    'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
    'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# 1. Create a DataFrame df from this dictionary data which has the index labels.
df = pd.DataFrame(data, index=labels)

# 2. Display a summary of the basic information about this DataFrame and its data.
print(df)
print(type(df))

# 3. Return the first 3 rows of the DataFrame df.
print(df[0:3])

# 4. Select just the 'animal' and 'age' columns from the DataFrame df.
print(df[['animal', 'age']])

# 5. Select the data in rows [3, 4, 8] and in columns ['animal', 'age'].
df_rows = df.iloc[[3, 4, 8]]
df_rows_and_columns = df_rows.loc[:, ['animal', 'age']]
print(df_rows_and_columns)

# 6. Select only the rows where the number of visits is greater than 3.

filtered_visits = df[df['visits'] > 3]
print(filtered_visits)

# 7. Select the rows where the age is missing, i.e. is NaN
df_ages = df[df['age'].isnull()]
print(df_ages)

# 8. Select the rows where the animal is a cat and the age is less than 3.
filtered_df = df[(df['animal'] == 'cat') & (df['age'] < 3)]
print(filtered_df)

# 9. Select the rows the age is between 2 and 4 (inclusive).
filtered_df = df[(df['age'] >= 2) & (df['age'] <= 4)]
print(filtered_df)

# 10. Change the age in row 'f' to 1.5.
df.loc[['f'], ['age']] = 1.5
print(df)

# 11. Calculate the sum of all visits (the total number of visits).
total_visits = df['visits'].sum()
print(total_visits)

# 12. Calculate the mean age for each different animal in df.
mean_age = df['age'].mean()
print(mean_age)

""" 13. Append a new row 'k' to df with your choice of values for each column. 
    Then delete that row to return the original DataFrame."""
df.loc['k'] = ['cat', 2.5, 1, 'yes']
print(df)

# 14. Count the number of each type of animal in df.
animal_count = df['animal'].value_counts()
print(animal_count)

""" 15. Sort df first by the values in the 'age' in descending order, 
    then by the value in the 'visit' column in ascending order."""
print(df.sort_values(['age'], ascending=False))
print(df.sort_values(['visits'], ascending=True))

""" 16. The 'priority' column contains the values 'yes' and 'no'. 
    Replace this column with a column of boolean values: 'yes' should be True and 'no' should be False."""
df['priority'] = df['priority'].replace(['yes'], [True])
df['priority'] = df['priority'].replace(['no'], [False])
print(df)
# 17. In the 'animal' column, change the 'snake' entries to 'python'.
df['animal'] = df['animal'].replace(['snake'], ['python'])
print(df)

""" 18. For each animal type and each number of visits, find the mean age. 
    In other words, each row is an animal, each column is a number of visits and 
    the values are the mean ages (hint: use a pivot table).
"""
