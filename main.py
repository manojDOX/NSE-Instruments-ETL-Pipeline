# nse_etl_pipeline/main.py

from etl.extract import download_and_load_data
from etl.transform import transform_data
from etl.load import load_to_mongo, load_to_sql
from etl.compare import generate_comparison_csvs


def run_pipeline():
    upstox_df, dhan_df = download_and_load_data()
    upstox_clean, dhan_clean = transform_data(upstox_df, dhan_df)
    load_to_mongo(upstox_clean)
    load_to_sql(dhan_clean)
    generate_comparison_csvs(upstox_clean, dhan_clean)


if __name__ == "__main__":
    run_pipeline()
