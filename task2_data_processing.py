import pandas as pd
import os
import glob

# Step 1: Find the JSON file created by Task 1


json_files = glob.glob("data/trends_*.json")

if not json_files:
    print("No trends JSON file found in the data folder.")
    exit()

# Use the most recently created JSON file
input_file = max(json_files, key=os.path.getmtime)


# Step 2: Load JSON into Pandas DataFrame

df = pd.read_json(input_file)

print(f"Loaded {len(df)} stories from {input_file}")


# Step 3: Remove duplicate stories
# Duplicate is identified using post_id


df = df.drop_duplicates(subset="post_id")

print(f"After removing duplicates: {len(df)}")



# Step 4: Remove rows with missing required values
# Required fields:
# post_id, title, score


df = df.dropna(
    subset=["post_id", "title", "score"]
)

print(f"After removing nulls: {len(df)}")



# Step 5: Clean data types
# Convert score and num_comments to numeric integers


df["score"] = pd.to_numeric(
    df["score"],
    errors="coerce"
)

df["num_comments"] = pd.to_numeric(
    df["num_comments"],
    errors="coerce"
)

# Remove rows where conversion failed
df = df.dropna(
    subset=["score", "num_comments"]
)

# Convert to integer
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)



# Step 6: Remove low-quality stories
# Keep only stories with score >= 5


df = df[df["score"] >= 5]

print(f"After removing low scores: {len(df)}")



# Step 7: Remove extra whitespace from titles


df["title"] = df["title"].str.strip()



# Step 8: Save cleaned data as CSV


output_file = "data/trends_clean.csv"

df.to_csv(
    output_file,
    index=False
)

print(f"\nSaved {len(df)} rows to {output_file}")


# Step 9: Print stories per category


print("\nStories per category:")

category_counts = df["category"].value_counts()

for category, count in category_counts.items():
    print(f"  {category:<16} {count}")
task2_data_processing.py
