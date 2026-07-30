import pandas as pd

# Load datasets
df = pd.read_csv("data/nhldraft.csv")

# First 5 rows
print(df.head())

# Columns
print(df.columns)

# Show size
print(df.size)

# Missing values
print(df.isnull().sum())
