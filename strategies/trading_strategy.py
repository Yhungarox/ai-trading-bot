class TradingStrategy:
    def __init__(self, model):
        self.model = model
    
    def make_trade_decision(self, prediction):
        # Based on prediction, decide whether to buy or sell
        if prediction == "buy":
            return "buy"
        elif prediction == "sell":
            return "sell"
        return "hold"
