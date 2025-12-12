from pymongo import MongoClient, UpdateOne
import sqlite3


def load_to_mongo(upstox_data):
    client = MongoClient('mongodb://localhost:27017/')
    db = client.market_data
    collection = db.upstox_nse

    operations = [
        UpdateOne({'instrument_key': row['instrument_key']},
                  {'$set': row.to_dict()}, upsert=True)
        for _, row in upstox_data.iterrows()
    ]
    collection.bulk_write(operations)
    client.close()


def load_to_sql(dhan_data):
    conn = sqlite3.connect('db/dhan_data.db')
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS dhan_nse")

    cursor.execute("""
            CREATE TABLE dhan_nse (
                SEM_TRADING_SYMBOL TEXT PRIMARY KEY,
                SEM_SMST_SECURITY_ID TEXT,
                SM_SYMBOL_NAME TEXT,
                exchange TEXT
            )
    """)


    for _, row in dhan_data.iterrows():
        cursor.execute("""
            INSERT OR REPLACE INTO dhan_nse (exchange, SEM_SMST_SECURITY_ID, SM_SYMBOL_NAME, SEM_TRADING_SYMBOL)
            VALUES (?, ?, ?, ?)
        """, tuple(row))

    conn.commit()
    conn.close()
