# Research Question 1: 
# Which team has the most NHL players drafted?
SELECT team, COUNT(*) AS players_drafted
FROM nhldraft
WHERE team IS NOT NULL
GROUP BY team
ORDER BY players_drafted DESC
LIMIT 1;

# Result: Montreal Canadiens | 627 

# Research Question 2:
# Which current NHL team has the highest average games played 
# per draft pick?
SELECT team, AVG(COALESCE(games_played, 0)) AS avg_games_played
FROM nhldraft
WHERE team IN (
    'Anaheim Ducks',
    'Boston Bruins',
    'Buffalo Sabres',
    'Calgary Flames',
    'Carolina Hurricanes',
    'Chicago Blackhawks',
    'Colorado Avalanche',
    'Columbus Blue Jackets',
    'Dallas Stars',
    'Detroit Red Wings',
    'Edmonton Oilers',
    'Florida Panthers',
    'Los Angeles Kings',
    'Minnesota Wild',
    'Montreal Canadiens',
    'Nashville Predators',
    'New Jersey Devils',
    'New York Islanders',
    'New York Rangers',
    'Ottawa Senators',
    'Philadelphia Flyers',
    'Pittsburgh Penguins',
    'San Jose Sharks',
    'Seattle Kraken',
    'St. Louis Blues',
    'Tampa Bay Lightning',
    'Toronto Maple Leafs',
    'Utah Mammoth',
    'Vancouver Canucks',
    'Vegas Golden Knights',
    'Washington Capitals',
    'Winnipeg Jets')
GROUP BY team
ORDER BY avg_games_played DESC
LIMIT 1;

# Result: Buffalo Sabres | 164.19

# Research Question 3:
# Which team has the highest average points per draft pick?
SELECT team, AVG(COALESCE(points, 0)) AS avg_points
FROM nhldraft
WHERE team IN (
    'Anaheim Ducks',
    'Boston Bruins',
    'Buffalo Sabres',
    'Calgary Flames',
    'Carolina Hurricanes',
    'Chicago Blackhawks',
    'Colorado Avalanche',
    'Columbus Blue Jackets',
    'Dallas Stars',
    'Detroit Red Wings',
    'Edmonton Oilers',
    'Florida Panthers',
    'Los Angeles Kings',
    'Minnesota Wild',
    'Montreal Canadiens',
    'Nashville Predators',
    'New Jersey Devils',
    'New York Islanders',
    'New York Rangers',
    'Ottawa Senators',
    'Philadelphia Flyers',
    'Pittsburgh Penguins',
    'San Jose Sharks',
    'Seattle Kraken',
    'St. Louis Blues',
    'Tampa Bay Lightning',
    'Toronto Maple Leafs',
    'Utah Mammoth',
    'Vancouver Canucks',
    'Vegas Golden Knights',
    'Washington Capitals',
    'Winnipeg Jets'
)
GROUP BY team
ORDER BY avg_points DESC
LIMIT 1;

# Result: Boston Bruins | 71.24