import pandas as pd

# Use a relative path if possible, or ensure the absolute path is correct
path = '/home/mirafra/Desktop/python_learnings/pandas/data.csv'

# Standard practice: Load the data and preview the first 5 rows
df = pd.read_csv(path)
print(df.head())

# Bonus: Check data types and missing values
print(df.info())
