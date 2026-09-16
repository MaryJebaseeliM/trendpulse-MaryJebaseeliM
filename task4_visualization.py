import pandas as pd
import matplotlib.pyplot as plt
import os

# --------------------------------------------------
# Task 4: TrendPulse Data Visualization
# --------------------------------------------------

# 1. Load the analysed CSV
df = pd.read_csv("data/trends_analysed.csv")

# Create outputs folder if it doesn't already exist
os.makedirs("outputs", exist_ok=True)


# --------------------------------------------------
# Chart 1: Top 10 Stories by Score
# --------------------------------------------------

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


# --------------------------------------------------
# Chart 2: Stories per Category
# --------------------------------------------------

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


# --------------------------------------------------
# Chart 3: Score vs Comments
# --------------------------------------------------

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


# --------------------------------------------------
# Bonus: TrendPulse Dashboard
# --------------------------------------------------

fig, axes = plt.subplots(2, 2, figsize=(16, 10))

# -------------------------
# Dashboard Chart 1
# -------------------------

axes[0, 0].barh(
    top_10["short_title"],
    top_10["score"]
)

axes[0, 0].set_xlabel("Score")
axes[0, 0].set_ylabel("Story Title")
axes[0, 0].set_title("Top 10 Stories by Score")

# Highest score at top
axes[0, 0].invert_yaxis()


# -------------------------
# Dashboard Chart 2
# -------------------------

axes[0, 1].bar(
    category_counts.index,
    category_counts.values,
    color=plt.cm.tab10(range(len(category_counts)))
)

axes[0, 1].set_xlabel("Category")
axes[0, 1].set_ylabel("Number of Stories")
axes[0, 1].set_title("Stories per Category")

axes[0, 1].tick_params(axis="x", rotation=45)


# -------------------------
# Dashboard Chart 3
# -------------------------

axes[1, 0].scatter(
    not_popular["score"],
    not_popular["num_comments"],
    label="Not Popular"
)

axes[1, 0].scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular"
)

axes[1, 0].set_xlabel("Score")
axes[1, 0].set_ylabel("Number of Comments")
axes[1, 0].set_title("Score vs Comments")
axes[1, 0].legend()


# -------------------------
# Empty fourth subplot
# -------------------------

axes[1, 1].axis("off")


# Overall dashboard title
fig.suptitle("TrendPulse Dashboard", fontsize=20)

plt.tight_layout()

# Save dashboard
plt.savefig(
    "outputs/dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()

print("\nAll charts created successfully!")
print("Saved files:")
print(" - outputs/chart1_top_stories.png")
print(" - outputs/chart2_categories.png")
print(" - outputs/chart3_scatter.png")
print(" - outputs/dashboard.png")