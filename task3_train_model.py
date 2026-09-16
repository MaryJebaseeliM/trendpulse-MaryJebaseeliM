# task3_train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# ---------------------------------------------------------
# 1. Load the dataset
# ---------------------------------------------------------

df = pd.read_csv("churnguard_data.csv")

print("Original shape:", df.shape)


# ---------------------------------------------------------
# 2. Task 2 Cleaning Steps
# ---------------------------------------------------------
# Apply ALL the cleaning steps from Task 2 here.
#
# Example:
# df = df.drop_duplicates()
# df = df.dropna()
#
# If you already had specific cleaning steps in Task 2,
# copy those exact steps here.


# ---------------------------------------------------------
# 3. Encode target column: Churn
# ---------------------------------------------------------

df["Churn"] = df["Churn"].map({
    "Yes": 1,
    "No": 0
})


# ---------------------------------------------------------
# 4. Encode categorical columns
# ---------------------------------------------------------

categorical_columns = [
    "gender",
    "PhoneService",
    "InternetService",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod"
]

df = pd.get_dummies(
    df,
    columns=categorical_columns,
    drop_first=True
)


# ---------------------------------------------------------
# 5. Separate X and y
# ---------------------------------------------------------

X = df.drop("Churn", axis=1)
y = df["Churn"]


# ---------------------------------------------------------
# 6. Split into training and testing data
# ---------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


print("Training data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)


# ---------------------------------------------------------
# 7. Train Logistic Regression model
# ---------------------------------------------------------

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)


# ---------------------------------------------------------
# 8. Make predictions
# ---------------------------------------------------------

y_pred = model.predict(X_test)


# ---------------------------------------------------------
# 9. Print accuracy
# ---------------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)


# ---------------------------------------------------------
# 10. Print classification report
# ---------------------------------------------------------

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=["Stay", "Churn"]
    )
)