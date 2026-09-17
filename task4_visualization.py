import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Load the analysed CSV
df = pd.read_csv("data/trends_analysed.csv")

# Create outputs folder if it doesn't already exist
os.makedirs("outputs", exist_ok=True)


# Chart 1: Top 10 Stories by Score


# Get the top 10 stories by score
top_10 = df.nlargest(10, "score").copy()

# Shorten titles longer than 50 characters
top_10["short_title"] = top_10["title"].apply(
    lambda title: title[:50] + "..." if len(title) > 50 else title
)

# Create horizontal bar chart
plt.figure(figsize=(10, 6))

plt.barh(top_10["short_title"], top_10["score"])

plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")

# Put highest score at the top
plt.gca().invert_yaxis()

plt.tight_layout()

# Save BEFORE show
plt.savefig("outputs/chart1_top_stories.png", dpi=300, bbox_inches="tight")
plt.show()

# Close the figure
plt.close()



# Chart 2: Stories per Category


# Count number of stories in each category
category_counts = df["category"].value_counts()

plt.figure(figsize=(10, 6))

# Different colour for each bar
plt.bar(
    category_counts.index,
    category_counts.values,
    color=plt.cm.tab10(range(len(category_counts)))
)

plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

# Rotate category names for readability
plt.xticks(rotation=45, ha="right")

plt.tight_layout()

# Save BEFORE show
plt.savefig("outputs/chart2_categories.png", dpi=300, bbox_inches="tight")
plt.show()

plt.close()


# Chart 3: Score vs Comments


plt.figure(figsize=(10, 6))

# Separate popular and non-popular stories
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

# Plot non-popular stories
plt.scatter(
    not_popular["score"],
    not_popular["num_comments"],
    label="Not Popular"
)

# Plot popular stories
plt.scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular"
)

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()

plt.tight_layout()

# Save BEFORE show
plt.savefig("outputs/chart3_scatter.png", dpi=300, bbox_inches="tight")
plt.show()

plt.close()

