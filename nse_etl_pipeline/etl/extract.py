import pandas as pd
import requests
import gzip
import io

UPSTOX_URL = "https://assets.upstox.com/market-quote/instruments/exchange/NSE.csv.gz"
DHAN_URL = "https://images.dhan.co/api-data/api-scrip-master.csv"


def download_and_load_data():
    # Download Upstox gzipped file
    upstox_response = requests.get(UPSTOX_URL)
    with gzip.open(io.BytesIO(upstox_response.content), 'rt') as f:
        upstox_df = pd.read_csv(f)

    # Download Dhan CSV
    dhan_response = requests.get(DHAN_URL)
    dhan_df = pd.read_csv(io.StringIO(dhan_response.text))

    return upstox_df, dhan_df
