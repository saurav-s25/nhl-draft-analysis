import pandas as pd
import sqlite3

# Read the CSV
df = pd.read_csv("data/nhldraft.csv")

# Connect to SQLite database
connection = sqlite3.connect("data/nhldraftdata.db")

# Put the dataframe into a SQL table
df.to_sql("nhldraft", connection, if_exists="replace", 
    index=False)

#Close connection
connection.close()

print("Database setup complete.")