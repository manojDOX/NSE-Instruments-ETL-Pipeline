from pymongo import MongoClient

def setup_mongo():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.market_data
    db.create_collection("upstox_nse")
    client.close()
