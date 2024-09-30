import time
import requests
from orderly_sdk import Orderly

class DataFeed:
    def __init__(self, api_key, secret_key):
        self.orderly = Orderly(api_key=api_key, secret_key=secret_key)

    def get_orderbook(self, symbol="BTC/USDT"):
        # Fetch live orderbook data from the Orderly Network SDK
        return self.orderly.get_orderbook(symbol)

    def execute_trade(self, symbol, side, amount):
        # Place an order on the Orderly Network
        return self.orderly.place_order(symbol, side, amount)