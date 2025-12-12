from extract import download_and_load_data
from transform import transform_data

def test_transform_data():
    # Step 1: Download raw data
    upstox_df, dhan_df = download_and_load_data()

    # Step 2: Transform
    upstox_clean, dhan_clean = transform_data(upstox_df, dhan_df)

    # Step 3: Check basic outputs
    print("✅ Transformed Upstox Data:")
    print(upstox_clean.head(), "\n")

    print("✅ Transformed Dhan Data:")
    print(dhan_clean.head(), "\n")


if __name__ == "__main__":
    test_transform_data()
