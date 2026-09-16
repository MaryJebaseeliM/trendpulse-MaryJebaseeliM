# Import pandas libraray
import pandas as pd

# 1. Load the dataset
df = pd.read_csv("C:\\Users\\Mary Moses\\churnguard_data.csv")
print(df)

# 2. Print the shape of the dataset
print("Shape of the dataset:")
print(df.shape)

# 3. Print the first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# 4. Print column names and data types
print("\nColumn names and data types:")
df.info()

# 5. Print the count of missing values in each column
print("\nMissing values in each column:")
print(df.isnull().sum())


# 6. Print the number of duplicate rows
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())


# 7. Print the value counts of the Churn column
print("\nValue counts of Churn:")
print(df["Churn"].value_counts())

# 8. Print the unique values in the Contract column
print("\nUnique values in Contract:")
print(df["Contract"].unique())
