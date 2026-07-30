import pandas as pd

# Load datasets
df = pd.read_csv("data/nhldraft.csv")

df = df.drop_duplicates()

# All players drafted
all_players = df.copy()

# All players that played >= 1 NHL game
nhl_players = df[df["games_played"].notna()].copy()

# print("All drafted players: ", all_players.shape)
# print("NHL players: ", nhl_players.shape)

print(df["team"].value_counts())