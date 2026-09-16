import pandas as pd
import numpy as np

# --------------------------------------------------
# Task 3: Load, Explore, Analyze and Save Trend Data
# --------------------------------------------------

# 1. Load the clean CSV file
df = pd.read_csv("data/trends_clean.csv")

# Print shape of the DataFrame
print(f"Loaded data: {df.shape}")

# Print first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Calculate average score and average comments
average_score = df["score"].mean()
average_comments = df["num_comments"].mean()

print(f"\nAverage score   : {average_score:,.2f}")
print(f"Average comments: {average_comments:,.2f}")


# --------------------------------------------------
# 2. Basic Analysis with NumPy
# --------------------------------------------------

# Convert score column to NumPy array
scores = df["score"].to_numpy()

# Calculate statistics using NumPy
mean_score = np.mean(scores)
median_score = np.median(scores)
std_score = np.std(scores)

highest_score = np.max(scores)
lowest_score = np.min(scores)

print("\n--- NumPy Stats ---")
print(f"Mean score   : {mean_score:,.2f}")
print(f"Median score : {median_score:,.2f}")
print(f"Std deviation: {std_score:,.2f}")
print(f"Max score    : {highest_score:,.2f}")
print(f"Min score    : {lowest_score:,.2f}")


# Find the category with the most stories
category_counts = df["category"].value_counts()

most_common_category = category_counts.idxmax()
most_common_category_count = category_counts.max()

print(
    f"\nMost stories in: {most_common_category} "
    f"({most_common_category_count} stories)"
)


# Find the story with the most comments
most_commented_index = df["num_comments"].idxmax()

most_commented_title = df.loc[most_commented_index, "title"]
most_commented_count = df.loc[most_commented_index, "num_comments"]

print(
    f'Most commented story: "{most_commented_title}" '
    f"— {most_commented_count:,} comments"
)


# --------------------------------------------------
# 3. Add New Columns
# --------------------------------------------------

# Engagement = comments / (score + 1)
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# is_popular is True when score is greater than average score
df["is_popular"] = df["score"] > average_score


# --------------------------------------------------
# 4. Save the Updated DataFrame
# --------------------------------------------------

df.to_csv("data/trends_analysed.csv", index=False)

print("\nSaved to data/trends_analysed.csv")