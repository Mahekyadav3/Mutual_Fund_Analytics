import yfinance as yf
ticker = yf.Ticker("INFY.NS")
history = ticker.history(period="1mo")
print(history.head())