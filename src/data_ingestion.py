import pandas as pd
import os
data_folder = "data/raw"
csv_files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]
for f in csv_files:
    file_path = os.path.join(data_folder, f)
    df = pd.read_csv(file_path)
    print("="*60)
    print(f"File: {f}")
    print("="*60)
    
    print("Shape:",df.shape)
    print("\nData Types:",df.dtypes)
    
    print("\nFrist 5 Rows:",df.head())
    print("\n")
    
    print("\nMissing Values:",df.isnull().sum())
    
    print("\nDuplicate Rows:",df.duplicated().sum())
    