import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)
#Convert date column
df['date'] = pd.to_datetime(df['date'])

#Sort data
df = df.sort_values(["amfi_code", "date"])
#Remove duplicates
df = df.drop_duplicates()

#Validate NAV > 0
invalid_nav = df[df["nav"]<= 0]

print("\nInvalid NAV Records:",len(invalid_nav))

#Keep only valid NAV values
df = df[df["nav"] > 0]

#Forward fill NAV values within each fund
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

#Save cleaned file 
df.to_csv(
    "data/processed/nav_history_clean.csv", 
    index=False
)
print("\nCleaned Shape:", df.shape)
print("\nNAV History Cleaning Completed")
