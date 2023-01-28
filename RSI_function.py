# import important libraries and functions
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import datetime
# custom functions
from get_today import get_today
from download_data import download_data


def calculate_rsi(
        start_date,
        end_date,
        symbol
    ):
        # get data for symbol
        data = download_data(start_date, end_date, symbol)

        # if we got data run RSI test, else don't do anything
        if data.empty:
            pass
        else:
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
