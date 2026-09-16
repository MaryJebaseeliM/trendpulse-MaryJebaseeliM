import pandas as pd
from sklearn.linear_model import LogisticRegression

# 1. Load dataset
df = pd.read_csv("churnguard_data.csv")

# 2. Basic cleaning
df = df.drop_duplicates()
df.columns = df.columns.str.strip()

# 3. Clean numeric columns
numeric_columns = [
    "tenure",
    "MonthlyCharges",
    "TotalCharges",
    "SeniorCitizen"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# 4. Encode Contract
df["Contract"] = (
    df["Contract"]
    .astype(str)
    .str.strip()
)

df["Contract"] = df["Contract"].map({
    "Month-to-month": 0,
    "One year": 1,
    "Two year": 2
})

# 5. Encode Churn
df["Churn"] = (
    df["Churn"]
    .astype(str)
    .str.strip()
    .str.lower()
    .map({
        "yes": 1,
        "no": 0
    })
)

# 6. Remove rows with missing values
features = [
    "tenure",
    "MonthlyCharges",
    "TotalCharges",
    "SeniorCitizen",
    "Contract"
]

df = df.dropna(subset=features + ["Churn"])

# 7. Prepare X and y
X = df[features]
y = df["Churn"]

# 8. Train model on the FULL cleaned dataset
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# 9. Get customer details
tenure = int(input("Enter tenure (months): "))

monthly_charges = float(
    input("Enter Monthly Charges: ")
)

total_charges = float(
    input("Enter Total Charges: ")
)

senior_citizen = int(
    input("Senior Citizen? (1 = Yes, 0 = No): ")
)

contract = int(
    input(
        "Contract type (0 = Month-to-month, "
        "1 = One year, 2 = Two year): "
    )
)

# 10. Create input for new customer
customer = pd.DataFrame([{
    "tenure": tenure,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges,
    "SeniorCitizen": senior_citizen,
    "Contract": contract
}])

# Make sure column order is correct
customer = customer[features]

# 11. Predict
prediction = model.predict(customer)[0]

# 12. Print required result
if prediction == 1:
    print("Prediction: This customer is likely to CHURN.")
else:
    print("Prediction: This customer is likely to STAY.")