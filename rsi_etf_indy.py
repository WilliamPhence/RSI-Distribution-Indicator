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
    print("\tSPY - S&P500")
    print("\tQQQ - NASDAQ 100")
    print("\tIWM - RUSSELL 2000")
    print("\tXLY - CONSUMER DISCRETIONARY")
    print("\tXLP - CONSUMER STAPLES")
    print("\tXLE - ENERGY")
    print("\tXLF - FINANCIALS")
    print("\tXLV - INDUSTRIALS")
    print("\tXLB - MATERIALS")
    print("\tXLRE - REAL ESTATE")
    print("\tXLK - TECHNOLOGY")
    print("\tXLU - UTILITIES")
    print("\tXLC - COMMUNICATION SERVICES")

    # Get user inputs
    etf = input("\nENTER ONE OF THE TICKERS : ")
    start_date = input("Enter the start date (YYYY-MM-DD) : ")
    end_date = input("Enter the end date (YYYY-MM-DD) or 't' for today : ")

    # convert end_date to correct format if user enters 'today'
    if end_date.upper() == 'T':
        end_date = date.today()
    else:
        end_date = end_date


    # call get_rsi_dist function and pass through user inputs
    data = get_rsi_dist(
            start_date,
            end_date,
            etf.upper(),
    )

    # Declare datasource
    df = pd.DataFrame(data)
    df.set_index('Date', inplace=True)

    plot_rsi_indy(df, etf, start_date, end_date)
    
    delete_temp_files(temp_data)


while True:
    rsi_etf_indy()
    repeat = input("Press 'Enter' to go again\nEnter anything else to exit : ")
    if repeat.upper() == "":
        continue
    else:
        break
