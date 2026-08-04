import pandas as pd
df = pd.read_csv("data/nhldraft.csv")
nhl_players = df[df["games_played"].notna()].copy()

# Research Question 1: 
# Which team has the most NHL players drafted?
(print (nhl_players["team"].value_counts().head(1)))

# Research Question 2:
# Which current NHL team has the highest average games played per draft pick?

# Players who never played in the NHL = 0 games
df["games_played"] = df["games_played"].fillna(0)

current_teams = [
    "Anaheim Ducks", "Arizona Coyotes", "Boston Bruins",
    "Buffalo Sabres", "Calgary Flames", "Carolina Hurricanes",
    "Chicago Blackhawks", "Colorado Avalanche",
    "Columbus Blue Jackets", "Dallas Stars", "Detroit Red Wings",
    "Edmonton Oilers", "Florida Panthers", "Los Angeles Kings",
    "Minnesota Wild", "Montreal Canadiens", "Nashville Predators",
    "New Jersey Devils", "New York Islanders", "New York Rangers",
    "Ottawa Senators", "Philadelphia Flyers",
    "Pittsburgh Penguins", "San Jose Sharks", "Seattle Kraken",
    "St. Louis Blues", "Tampa Bay Lightning",
    "Toronto Maple Leafs", "Vancouver Canucks",
    "Vegas Golden Knights"]

avg_games_by_pick = (df[df["team"].isin(current_teams)]
    .groupby("team")["games_played"]
    .mean()
    .sort_values(ascending=False))

# Team with most games played per pick
(print(avg_games_by_pick.head(1)))

# Research Question 3:
# Which team has the highest average points per draft pick?

df["points"] = df["points"].fillna(0)

avg_points_by_pick = (df[df["team"].isin(current_teams)]
    .groupby("team")["points"]
    .mean()
    .sort_values(ascending=False))

print(avg_points_by_pick.head(1))

