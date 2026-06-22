import requests
import pandas as pd
import os

# Dictionary containing scheme names and their AMFI codes
schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

# Create folder if it doesn't exist
output_folder = "data/raw/live_nav"
os.makedirs(output_folder, exist_ok=True)

# Fetch data for each scheme
for scheme_name, amfi_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{amfi_code}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Convert NAV history to DataFrame
        nav_df = pd.DataFrame(data["data"])

        # Save CSV
        file_path = f"{scheme_name}.csv"
        file_path = os.path.join(output_folder, file_path)
        nav_df.to_csv(file_path, index=False)

        print(f"{scheme_name} data saved successfully.")

    else:
        print(f"Failed to fetch {scheme_name}")
print("All data fetching completed.")