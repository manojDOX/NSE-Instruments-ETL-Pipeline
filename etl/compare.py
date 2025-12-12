import pandas as pd

def generate_comparison_csvs(upstox, dhan):
    upstox_set = set(upstox['tradingsymbol'])
    dhan_set = set(dhan['SEM_TRADING_SYMBOL'])

    common_symbols = upstox_set & dhan_set
    only_upstox = upstox_set - dhan_set
    only_dhan = dhan_set - upstox_set

    common_df = pd.merge(
        upstox[upstox['tradingsymbol'].isin(common_symbols)],
        dhan[dhan['SEM_TRADING_SYMBOL'].isin(common_symbols)],
        left_on='tradingsymbol',
        right_on='SEM_TRADING_SYMBOL',
        suffixes=('_upstox', '_dhan')
    )
    common_df.to_csv('output/common_stocks.csv', index=False)

    upstox[upstox['tradingsymbol'].isin(only_upstox)].to_csv('output/only_in_upstox.csv', index=False)
    dhan[dhan['SEM_TRADING_SYMBOL'].isin(only_dhan)].to_csv('output/only_in_dhan.csv', index=False)
