def transform_data(upstox_df, dhan_df):
    # Filter NSE EQ
    upstox_df = upstox_df[(upstox_df['exchange'].str.startswith('NSE')) & (upstox_df['instrument_type'] == 'EQUITY')]
    dhan_df = dhan_df[(dhan_df['SEM_EXM_EXCH_ID'] == 'NSE') & (dhan_df['SEM_INSTRUMENT_NAME'] == 'EQUITY')]

    # Normalize trading symbol
    upstox_df['tradingsymbol'] = upstox_df['tradingsymbol'].str.strip().str.upper()
    dhan_df['SEM_TRADING_SYMBOL'] = dhan_df['SEM_TRADING_SYMBOL'].str.strip().str.upper()

    # List of columns you want
    upstox_wanted_cols = ['instrument_key', 'tradingsymbol', 'short_name', 'name', 'isin']
    # Filter to only those present
    upstox_present = [col for col in upstox_wanted_cols if col in upstox_df.columns]
    # Copy only those columns
    upstox_clean = upstox_df[upstox_present].copy()
    # Add 'exchange' column
    upstox_clean['exchange'] = 'NSE'

    dhan_required = ['SM_SYMBOL_NAME', 'SEM_SMST_SECURITY_ID', 'SEM_TRADING_SYMBOL']
    dhan_available = [col for col in dhan_required if col in dhan_df.columns]

    dhan_clean = dhan_df[dhan_available].copy()
    dhan_clean['exchange'] = 'NSE'


    """ # Rename fields
    upstox_clean.rename(columns={'symbol': 'symbol_name'}, inplace=True)
    dhan_clean.rename(columns={
        'SM_SYMBOL_NAME': 'symbol_name',
        'SEM_SMST_SECURITY_ID': 'security_id'
    }, inplace=True) """

    return upstox_clean, dhan_clean
