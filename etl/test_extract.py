import pandas as pd
from extract import download_and_load_data

def test_download_and_load_data():
    upstox_df, dhan_df = download_and_load_data()
    
    # Basic sanity checks
    print("✅ Upstox DataFrame:")
    print(upstox_df.head(), "\n")
    print(f"Rows: {len(upstox_df)}, Columns: {len(upstox_df.columns)}\n")

    print("✅ Dhan DataFrame:")
    print(dhan_df.head(), "\n")
    print(f"Rows: {len(dhan_df)}, Columns: {len(dhan_df.columns)}")

if __name__ == "__main__":
    test_download_and_load_data()
