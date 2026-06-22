import pandas as pd
import requests
url = "https://api.mfapi.in/mf/125497"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    
    print("Meta Information:")
    print(data["meta"])
    
    nav_df = pd.DataFrame(data["data"])
    
    print("\nFirst 5 Rows of NAV Data:")
    print(nav_df.head())
    
    nav_df.to_csv("data/raw/nav_data.csv", index=False)
    print("\nNAV data saved to successfully")
else:
    print("Failed to fetch data. Status code:", response.status_code)
    