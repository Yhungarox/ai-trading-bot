class TradingStrategy:
    def __init__(self, model, stop_loss_threshold=0.02, take_profit_threshold=0.05):
        self.model = model
        self.stop_loss_threshold = stop_loss_threshold
        self.take_profit_threshold = take_profit_threshold
        self.entry_price = None

    def make_trade_decision(self, current_price, prediction):
        if prediction == "buy":
            self.entry_price = current_price
            return "buy"
        elif prediction == "sell":
            self.entry_price = None
            return "sell"
        return "hold"

    def apply_risk_management(self, current_price):
        if self.entry_price:
            price_change = (current_price - self.entry_price) / self.entry_price
            if price_change <= -self.stop_loss_threshold:
                return "sell"  # Trigger stop-loss
            elif price_change >= self.take_profit_threshold:
                return "sell"  # Trigger take-profit
        return "hold"
