import pandas as pd

# Read CSV
df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# Convert transaction_date to datetime
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Remove duplicates
df = df.drop_duplicates()

# Validate amount > 0
invalid_amount = df[df["amount_inr"] <= 0]

print("\nInvalid Amount Records:")
print(len(invalid_amount))

# Keep only valid amounts
df = df[df["amount_inr"] > 0]

# Validate KYC status
valid_kyc = ["Verified", "Pending", "Rejected"]

invalid_kyc = df[~df["kyc_status"].isin(valid_kyc)]

print("\nInvalid KYC Records:")
print(len(invalid_kyc))

# Save cleaned file
df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("\nCleaned Shape:", df.shape)
print("\nInvestor Transactions Cleaning Completed")
