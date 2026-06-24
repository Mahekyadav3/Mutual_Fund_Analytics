import pandas as pd
from sqlalchemy import create_engine
#create SQLite database engine
engine = create_engine("sqlite:///bluestock_mf.db")

#load cleaned csv files
nav_df = pd.read_csv("data/processed/nav_history_clean.csv")
transactions_df = pd.read_csv("data/processed/investor_transactions_clean.csv")
performance_df = pd.read_csv("data/processed/scheme_performance_clean.csv")

#save to SQLite tables
nav_df.to_sql("fact_nav",engine,if_exists="replace",index=False)
transactions_df.to_sql("fact_transactions",engine,if_exists="replace",index=False)
performance_df.to_sql("fact_performance",engine,if_exists="replace",index=False)

print("Database created successfully and data loaded into tables.")

print("\nRow Counts:")
print("fact_nav:",len(nav_df))
print("fact_transactions:",len(transactions_df))
print("fact_performance:",len(performance_df))