import pandas as pd

# 1. Load the dataset
df = pd.read_csv("churnguard_data.csv")

# 2. Drop customerID
df = df.drop("customerID", axis=1)

# 3. Remove duplicate rows
df = df.drop_duplicates()

# 4. Strip whitespace
df["gender"] = df["gender"].str.strip()
df["PaymentMethod"] = df["PaymentMethod"].str.strip()

# 5. Standardise casing
df["Churn"] = df["Churn"].str.strip().str.title()
df["PhoneService"] = df["PhoneService"].str.strip().str.title()
df["PaperlessBilling"] = df["PaperlessBilling"].str.strip().str.title()

# 6. Fix Contract variations
contract_map = {
    "Monthly": "Month-to-month",
    "month to month": "Month-to-month",
    "Month to month": "Month-to-month",
    "month-to-month": "Month-to-month",
    "Month-to-month": "Month-to-month",
    "1 year": "One year",
    "one year": "One year",
    "One Year": "One year",
    "2 year": "Two year",
    "two year": "Two year",
    "Two Year": "Two year"
}

df["Contract"] = (
    df["Contract"]
    .str.strip()
    .map(contract_map)
)

# 7. Fix InternetService variations
internet_map = {
    "dsl": "DSL",
    "DSL": "DSL",
    "Fibre optic": "Fiber optic",
    "Fiber optic": "Fiber optic",
    "FiberOptic": "Fiber optic",
    "fiber optic": "Fiber optic",
    "None": "No",
    "none": "No",
    "No": "No",
    "no": "No"
}

df["InternetService"] = (
    df["InternetService"]
    .str.strip()
    .map(internet_map)
)

# 8. Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# 9. Remove rows where tenure is zero or negative
df = df[df["tenure"] > 0]

# 10. Remove rows where MonthlyCharges is less than 10 or greater than 200
df = df[
    (df["MonthlyCharges"] >= 10) &
    (df["MonthlyCharges"] <= 200)
]

# 11. Fill missing values
df["MonthlyCharges"] = df["MonthlyCharges"].fillna(
    df["MonthlyCharges"].mean()
)

df["TotalCharges"] = df["TotalCharges"].fillna(
    df["TotalCharges"].mean()
)

df["tenure"] = df["tenure"].fillna(
    round(df["tenure"].median())
).astype(int)

# 12. Print shape of cleaned DataFrame
print("Shape of cleaned DataFrame:")
print(df.shape)

# 13. Print missing value counts
print("\nMissing value counts:")
print(df.isnull().sum())