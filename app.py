import time
import pandas as pd
import numpy as np
from empyreal_sdk import Empyreal
from orderly_sdk import Orderly
from models.model import TradingModel
from strategies.trading_strategy import TradingStrategy
from config import ORDERLY_API_KEY, ORDERLY_SECRET_KEY, EMPYREAL_API_KEY

# Initialize SDKs
empyreal = Empyreal(api_key=EMPYREAL_API_KEY)
orderly = Orderly(api_key=ORDERLY_API_KEY, secret_key=ORDERLY_SECRET_KEY)

# Initialize trading model and strategy
model = TradingModel()
strategy = TradingStrategy(model)

# Main trading loop
def run_trading_bot():
    while True:
        # Fetch market data
        market_data = orderly.get_orderbook("BTC/USDT")  # Replace with the desired asset
        print("Market Data:", market_data)
        
        # Process data and make predictions
        prediction = model.predict(market_data)
        print("Model Prediction:", prediction)
        
        # Execute trade based on prediction
        decision = strategy.make_trade_decision(prediction)
        print("Trade Decision:", decision)
        
        if decision == "buy":
            orderly.place_order("BTC/USDT", "buy", 1)
        elif decision == "sell":
            orderly.place_order("BTC/USDT", "sell", 1)
        
        # Wait before the next iteration
        time.sleep(10)

if __name__ == "__main__":
    run_trading_bot()
