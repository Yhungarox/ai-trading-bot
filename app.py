import time
from config import ORDERLY_API_KEY, ORDERLY_SECRET_KEY
from data.data_feed import DataFeed
from models.model import TradingModel
from strategies.trading_strategy import TradingStrategy

# Initialize components
data_feed = DataFeed(api_key=ORDERLY_API_KEY, secret_key=ORDERLY_SECRET_KEY)
model = TradingModel()
strategy = TradingStrategy(model)

# Main trading loop
def run_trading_bot():
    while True:
        # Fetch market data
        market_data = data_feed.get_orderbook(symbol="BTC/USDT")
        current_price = market_data["bids"][0][0]

        # Predict market movement
        prediction = model.predict(market_data)
        print("Model Prediction:", prediction)

        # Make trade decision based on prediction
        decision = strategy.make_trade_decision(current_price, prediction)
        print("Trade Decision:", decision)

        # Apply risk management
        risk_decision = strategy.apply_risk_management(current_price)
        if risk_decision == "sell":
            decision = risk_decision
            print("Risk management triggered:", decision)

        # Execute trade
        if decision == "buy":
            data_feed.execute_trade("BTC/USDT", "buy", 1)
        elif decision == "sell":
            data_feed.execute_trade("BTC/USDT", "sell", 1)

        time.sleep(10)  # Pause before fetching the next data
