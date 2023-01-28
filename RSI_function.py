# import important libraries and functions
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import datetime
# custom functions
from get_today import get_today


def calculate_rsi(
        start_date,
        end_date,
        symbol
    ):

    try:
        # Apply yf override function
        yf.pdr_override()

        # Obtain data, show terminal output for each download attempt
        print(f"Getting Yahoo Data for {symbol}....")
        data = pdr.get_data_yahoo(symbol, start_date, end_date)['Close']
        # Take the data we just downloaded and put it into a pandas dataframe
        data = pd.DataFrame(data)

        # Change Indexing from dates to integers
        data = data.reset_index(names="Date")
        
        # Convert Datetime formats
        data['Date'] = pd.to_datetime(data['Date'], utc=True).dt.date


        # Get today's date and time to see if we need to get today's data
        now = datetime.datetime.now()
        weekday = now.weekday()
        hour = now.hour
        if weekday >= 1 and weekday <= 4:
            if hour >= 17:
                today = get_today(symbol)
                data = pd.concat([data, today], ignore_index=True)
                pass


        # Calculate Gain
        Delta = data['Close'].diff()
        # Create Up and Down Columns to keep track of gains and losses and their values
        Up = Delta.clip(lower=0)
        Down = (-1)*Delta.clip(upper=0)
        # Calculate the moving averages
        sma_up = Up.rolling(14).mean()
        sma_down = Down.rolling(14).mean()
        # Calculate the relative strength
        rs = sma_up / sma_down
        # Calculate RSI
        rsi = 100 - ( 100 / ( 1 + rs ))
    
        # Create a column that tells us if RSI is > 50 or not
        data.loc[rsi <= 50, 'RSI_test'] = 'N'
        data.loc[rsi > 50, 'RSI_test'] = 'Y'

        # Remove Rows without RSI value
        data = data.dropna()
        return data

    except ValueError:
        print(f"Failed to download {symbol} DATA")
        print(data)
