# Import Libraries and functions
from get_rsi_distributions import get_rsi_dist
from delete_temp_files import delete_temp_files
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import date
import pandas as pd

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

# Declare Plot variables
def plot_rsi_indy(df):
    # Declare figure and axes variables
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    line_name = f'{etf.upper()}_Close'

    line_etf, = ax1.plot(
            df[line_name], 
            label='SPY',
            )
    line_rsi_y, = ax2.plot(
            df['Y'], 
            label='%'+' of SPY Components w/ RSI over 50',
            c='red'
            )

    # Plot lines & format figure
    # Format and create legend
    fig.legend(
        (
        line_etf, 
        line_rsi_y, 
        ), 
        (
        f'{etf.upper()}',
        '%'+f' of {etf.upper()} Components w/ RSI over 50', 
        ),
        loc='upper right',
    )

    # Format the axes
    ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b\n%Y'))
    ax1.set_title(f'{etf.upper()} vs {etf.upper()} Components RSI Distribution')
    ax1.set_ylabel(f"{etf.upper()}")
    ax2.set_ylabel('%'+f' of {etf.upper()} Comp. w/ RSI > 50')
    ax1.set_xlabel('Dates (Month-Year)')
   
    print(df)

    # Save the figures and show the plots    
    plt.savefig(f"C:\Python Projects\RSI Indicator\\figures\{etf} RSI Distributions.png", dpi=1000, bbox_inches='tight', pad_inches=0.5)
    plt.show()

    delete_temp_files(temp_data)


# show and save plot
plot_rsi_indy(df)