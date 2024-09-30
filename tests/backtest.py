import pandas as pd
from models.model import TradingModel
from strategies.trading_strategy import TradingStrategy

# Load historical data (example CSV format)
historical_data = pd.read_csv('btc_usd_historical.csv')

# Initialize model and strategy
model = TradingModel()
strategy = TradingStrategy(model)

# Track performance metrics
balance = 1000  # Starting balance in USD
profit_loss = 0

for index, row in historical_data.iterrows():
    current_price = row['price']
    market_data = {'price': current_price}
    
    # Model prediction
    prediction = model.predict(market_data)

    # Make trade decision
    decision = strategy.make_trade_decision(current_price, prediction)

    # Apply risk management
    risk_decision = strategy.apply_risk_management(current_price)
    if risk_decision == "sell":
        decision = risk_decision

    # Simulate trade execution
    if decision == "buy":
        balance -= current_price
    elif decision == "sell":
        balance += current_price

# Calculate profit/loss and other metrics (e.g., Sharpe ratio)
print("Final Balance:", balance)
