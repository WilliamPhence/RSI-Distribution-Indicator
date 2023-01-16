# Import Libraries and functions
from get_rsi_distributions import get_rsi_dist
from plot_rsi_indicator import plot_rsi_indy
from delete_temp_files import delete_temp_files
from datetime import date
import pandas as pd



def rsi_etf_indy():

    # Declare path for the temp data to be deleted after plots are shown and saved
    temp_data = 'C:\Python Projects\RSI Indicator\DATA'

    # ask use to select from a menu of ETFs
    print("You can select from one of the following ETF's to plot the RSI Distribution indicator for:")
    print("SPY - S&P500")
    print("QQQ - NASDAQ 100")
    print("IWM - RUSSELL 2000")
    print("XLY - CONSUMER DISCRETIONARY")
    print("XLP - CONSUMER STAPLES")
    print("XLY - FINANCIALS")
    print("XLV - INDUSTRIALS")
    print("XLB - MATERIALS")
    print("XLRE - REAL ESTATE")
    print("XLK - TECHNOLOGY")
    print("XLU - UTILITIES")
    print("XLC - COMMUNICATION SERVICES")

    # Get user inputs
    etf = input("\nENTER ONE OF THE TICKERS : ")
    start_date = input("Enter the start date (YYYY-MM-DD) : ")
    end_date = input("Enter the end date (YYYY-MM-DD) or 'today' : ")

    # convert end_date to correct format if user enters 'today'
    if end_date.upper() == 'TODAY':
        end_date = date.today()
    else:
        end_date = end_date


    # call get_rsi_dist function and pass through user inputs
    get_rsi_dist(
            start_date,
            end_date,
            etf.upper(),
    )

    # Declare datasource
    df = pd.read_pickle(f"C:\Python Projects\RSI Indicator\DATA\ 000_FINAL_DATA.pkl") 
    # Set datasource as a dataframe and set date column as the index
    df = pd.DataFrame(df)
    df.set_index('Date', inplace=True)

    plot_rsi_indy(df, etf, start_date, end_date)
    
    delete_temp_files(temp_data)

loop = True   
while True:
    rsi_etf_indy()
    repeat = input("Are you done? Y/N : ")
    if repeat.upper() == "N":
        continue
    elif repeat.upper() == 'Y':
        break
