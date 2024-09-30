import time
import requests
from orderly_sdk import Orderly

class DataFeed:
    def __init__(self, api_key, secret_key):
        self.orderly = Orderly(api_key=api_key, secret_key=secret_key)

    def get_market_data(self, symbol="BTC/USDT"):
        # Fetch live orderbook data from the Orderly Network
        orderbook = self.orderly.get_orderbook(symbol)
        return orderbook

    def simulate_data_feed(self, symbol="BTC/USDT"):
        # Simulate a simple data feed (replace with actual API call)
        while True:
            print(f"Fetching market data for {symbol}")
            data = self.get_market_data(symbol)
            yield data
            time.sleep(5)
