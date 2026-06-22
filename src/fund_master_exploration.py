import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv") 
print("=" * 60)
print("Unique Fund Houses")
print("=" * 60)
print(fund_master["fund_house"].unique())
print(f"\nTotal Fund Houses: {fund_master['fund_house'].nunique()}")

print("\n" + "=" * 60)
print("Unique Categories")
print("=" * 60)
print(fund_master["category"].unique())
print(f"\nTotal Categories: {fund_master['category'].nunique()}")

print("\n" + "=" * 60)
print("Unique Sub-Categories")
print("=" * 60)
print(fund_master["sub_category"].unique())
print(f"\nTotal Sub-Categories: {fund_master['sub_category'].nunique()}")

print("\n" + "=" * 60)
print("Unique Risk Categories")
print("=" * 60)
print(fund_master["risk_category"].unique())
print(f"\nTotal Risk Categories: {fund_master['risk_category'].nunique()}")

print("\n" + "=" * 60)
print("AMFI Scheme Codes")
print("=" * 60)
print(fund_master["amfi_code"].head(10))