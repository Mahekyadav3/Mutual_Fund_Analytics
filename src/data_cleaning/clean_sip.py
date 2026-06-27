import pandas as pd

df = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

df = df.drop_duplicates()

df.to_csv(
    "data/processed/04_monthly_sip_inflows_clean.csv",
    index=False
)