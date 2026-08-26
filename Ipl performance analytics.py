import numpy as np
import pandas as pd

# IPL player data
players = np.array([
    [450, 15, 12],
    [520, 18, 15],
    [300, 10, 8],
    [650, 20, 18],
    [400, 14, 10]
])


# 1. Average runs scored
average_runs = np.mean(players[:, 0])

print("Average runs scored:")
print(average_runs)


# 2. Highest run scorer
highest_runs = np.argmax(players[:, 0])

print("\nHighest run scorer:")
print("Player", highest_runs + 1)
print("Runs:", players[highest_runs, 0])


# 3. Lowest run scorer
lowest_runs = np.argmin(players[:, 0])

print("\nLowest run scorer:")
print("Player", lowest_runs + 1)
print("Runs:", players[lowest_runs, 0])


# 4. Highest wicket taker
highest_wickets = np.argmax(players[:, 2])

print("\nHighest wicket taker:")
print("Player", highest_wickets + 1)
print("Wickets:", players[highest_wickets, 2])


# 5. Runs per match for each player
runs_per_match = players[:, 0] / players[:, 1]

print("\nRuns per match:")
print(runs_per_match)


# 6. Players with more than 400 runs
more_than_400 = np.where(players[:, 0] > 400)

print("\nPlayers with more than 400 runs:")
print(more_than_400[0] + 1)


# 7. Players with more than 10 wickets
more_than_10 = np.where(players[:, 2] > 10)

print("\nPlayers with more than 10 wickets:")
print(more_than_10[0] + 1)


# 8. Standard deviation of runs
runs_std = np.std(players[:, 0])

print("\nStandard deviation of runs:")
print(runs_std)


# 9. Classify players based on runs
status = np.where(
    players[:, 0] >= 500,
    "Excellent",
    np.where(players[:, 0] >= 400, "Good", "Average")
)

print("\nPlayer classification:")
print(status)


# 10. Convert results into Pandas DataFrame
df = pd.DataFrame(
    players,
    columns=["Runs", "Matches", "Wickets"]
)

df["Runs Per Match"] = runs_per_match
df["Status"] = status

print("\nFinal DataFrame:")
print(df)