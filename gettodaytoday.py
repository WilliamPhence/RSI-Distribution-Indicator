import requests
import json
from datetime import date
import pandas as pd


def gettodaytoday(ticker):
    api_key = "V963FWMYLF1FNKIW"
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&apikey={api_key}"

    response = requests.get(url)

    data = json.loads(response.text)

    today = date.today()

    closing_price = data['Time Series (Daily)'][str(today)]['4. close']
    closing_price = float(closing_price)
    print(closing_price)

    df = {
        "Date":[today],
        "Close": [closing_price]
        }
    df = pd.DataFrame(df)
    df.to_pickle('C:\Python Projects\RSI Indicator\DATA\\todays close DATA.pkl')
    print(df)