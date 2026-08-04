import pandas as pd

# Load datasets
df = pd.read_csv("data/nhldraft.csv")

# First 5 rows
# print(df.head())

# Columns
# print(df.columns)

# Missing values
# print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# All players drafted 
all_players = df.copy()

# Players who played at least one game in the NHL
nhl_players = df[df["games_played"].notna()].copy()

print("All drafted players:", all_players.shape)
print("NHL players:", nhl_players.shape)

# Number of NHL players drafted by each time
(print (nhl_players["team"].value_counts()))