import numpy as np
import pandas as pd

# Movie rating data
ratings = np.array([
    [8.5, 120000],
    [7.8, 95000],
    [9.1, 180000],
    [6.9, 70000],
    [8.2, 110000]
])


# 1. Average movie rating
average_rating = np.mean(ratings[:, 0])

print("Average movie rating:")
print(average_rating)


# 2. Highest-rated movie
highest_rating = np.argmax(ratings[:, 0])

print("\nHighest-rated movie:")
print("Movie", highest_rating + 1)
print("Rating:", ratings[highest_rating, 0])


# 3. Lowest-rated movie
lowest_rating = np.argmin(ratings[:, 0])

print("\nLowest-rated movie:")
print("Movie", lowest_rating + 1)
print("Rating:", ratings[lowest_rating, 0])


# 4. Movies with rating greater than 8
above_8 = np.where(ratings[:, 0] > 8)

print("\nMovies with rating greater than 8:")
print(above_8[0] + 1)


# 5. Movies with more than 100000 votes
above_100000 = np.where(ratings[:, 1] > 100000)

print("\nMovies with more than 100000 votes:")
print(above_100000[0] + 1)


# 6. Movie with maximum number of votes
maximum_votes = np.argmax(ratings[:, 1])

print("\nMovie with maximum votes:")
print("Movie", maximum_votes + 1)
print("Votes:", int(ratings[maximum_votes, 1]))


# 7. Standard deviation of ratings
rating_std = np.std(ratings[:, 0])

print("\nStandard deviation of ratings:")
print(rating_std)


# 8. Classify movies based on rating
status = np.where(
    ratings[:, 0] >= 8.5,
    "Excellent",
    np.where(ratings[:, 0] >= 7.5, "Good", "Average")
)

print("\nMovie classification:")
print(status)


# 9. Convert data into Pandas DataFrame
df = pd.DataFrame(
    ratings,
    columns=["Rating", "Number of Votes"]
)

df["Status"] = status

print("\nFinal DataFrame:")
print(df)


# 10. Sort DataFrame by rating
df = df.sort_values("Rating", ascending=False)

print("\nDataFrame sorted by rating:")
print(df)