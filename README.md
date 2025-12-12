# NSE ETL Pipeline

## Setup Instructions

1. Clone repo & install dependencies:
pip install -r requirements.txt

2. Run pipeline:
python main.py


3. Ensure MongoDB is running and SQLite DB is created automatically.

## Output

- `common_stocks.csv`
- `only_in_upstox.csv`
- `only_in_dhan.csv`

## Assumptions

- Trading symbol is treated as the unique key for matching.
