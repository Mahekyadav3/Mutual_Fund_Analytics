import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

#get unique amfi codes
fund_master_codes = set(fund_master["amfi_code"])
nav_history_codes = set(nav_history["amfi_code"])

#check missing codes
missing_codes = fund_master_codes - nav_history_codes
print("="*60)
print("AMFI code validation")
print("="*60)

print(f"Total AMFI codes in Fund Master: {len(fund_master_codes)}")
print(f"Total AMFI codes in NAV History: {len(nav_history_codes)}")
if len(missing_codes) == 0:
    print("\nAll AMFI codes from Fund Master are present in NAV History.")
else:
    print(f"\nMissing AMFI Codes: {len(missing_codes)}")
    print(missing_codes)