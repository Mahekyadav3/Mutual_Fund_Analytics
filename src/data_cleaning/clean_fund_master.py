import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

df = df.drop_duplicates()

df.to_csv(
    "data/processed/01_fund_master_clean.csv",
    index=False
)