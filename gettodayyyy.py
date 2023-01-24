import yfinance as yf
import pandas as pd
from datetime import date

#This is currently not in production

def get_today(ticker):

    ticker_yahoo = yf.Ticker(ticker)
    data = ticker_yahoo.history()

    last_quote = data['Close'].iloc[1]
    today = date.today()

    df = pd.DataFrame({'Date':[today], 'Close':[last_quote]})
    return df