import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "nba.csv"  # Replace with the path to your CSV file
df = pd.read_csv(file_path, sep=';')

# 1. Identify the player with the most points scored in the playoffs
most_points_player = df.loc[df['PTS'].idxmax()]
print(f"Player with the most points scored in the playoffs: {most_points_player['Player']} ({most_points_player['PTS']} points)")

# 2. Compare average points per game across teams
average_points_per_team = df.groupby('Tm')['PTS'].mean().sort_values(ascending=False)
print("\nAverage points per game across teams:")
print(average_points_per_team)

# 3. Create a chart showing performance trends of the top 5 players across games
top_5_players = df.nlargest(5, 'PTS')
plt.figure(figsize=(10, 6))
for _, player in top_5_players.iterrows():
    plt.plot(player['G'], player['PTS'], marker='o', label=player['Player'])

plt.title("Performance Trends of Top 5 Players Across Games", fontsize=16)
plt.xlabel("Games Played", fontsize=12)
plt.ylabel("Points Scored", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()

# 4. Analyze the average number of fouls committed by each team
average_fouls_per_team = df.groupby('Tm')['PF'].mean().sort_values(ascending=False)
print("\nAverage number of fouls committed by each team:")
print(average_fouls_per_team)

# 5. Identify the player with the greatest overall contribution (points + assists)
df['Total Contribution'] = df['PTS'] + df['AST']
greatest_contributor = df.loc[df['Total Contribution'].idxmax()]
print(f"\nPlayer with the greatest overall contribution: {greatest_contributor['Player']} ({greatest_contributor['Total Contribution']} points + assists)")
