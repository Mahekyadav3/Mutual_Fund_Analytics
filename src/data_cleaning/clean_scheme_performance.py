import pandas as pd

# Read CSV
df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Return columns to validate
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

# Ensure returns are numeric
for col in return_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Check for anomalies
anomalies = df[
    (df["return_1yr_pct"] > 100) |
    (df["return_1yr_pct"] < -100)
]

print("\nAnomalous Return Records:")
print(len(anomalies))

# Expense ratio validation
expense_issues = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nExpense Ratio Issues:")
print(len(expense_issues))

# Save cleaned file
df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("\nCleaned Shape:", df.shape)
print("\nScheme Performance Cleaning Completed")
