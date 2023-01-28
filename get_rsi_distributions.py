# import important libraries and functions
import pandas as pd
from RSI_function import calculate_rsi
from download_data import download_data
from get_symbols import get_symbol_list


# Grab data and run RSI test 
def get_rsi_dist(        
        start_date,
        end_date,
        etf,
    ):
    # Grab user selected ETF data
    main_df = download_data(        
        start_date,
        end_date,
        etf,
    )
    main_df = pd.DataFrame(main_df)
    # Rename close column in main
    new_name = f"{etf}_Close"
    main_df.rename(columns={'Close':new_name}, inplace=True)   

    # create an empty list to store symbols with failed downloads
    failed_downloads = []

    # Get the list of symbols for the components of the ETF chosen
    symbols = get_symbol_list(etf)
    # format string list to have no extra spaces
    symbols = [symbol.rstrip() for symbol in symbols]    
    symbol_count = int(len(symbols)) 

    # Run RSI function for each symbol
    for i, symbol in enumerate(symbols):
        
        print(f"Request {i + 1} of {symbol_count} for {symbol}...")
        # Download data for all symbols and see if RSI is over 50 or not
        # This function also creates a dataframe for each symbol that is used in the try block below
        data = calculate_rsi(
                start_date,
                end_date, 
                symbol
        )

        # Add each Symbol's RSI_test results to a main data frame that contains SPY & Date Data
        try: 
            # pass each new dataframe into a temporary data frame
            data = pd.DataFrame(data)

            # Reduce data frame to only needed columns
            data = data[['Date','RSI_test']]

            # Rename Column headers
            new_name = f"{symbol}_rsi_test"
            data.rename(columns= {'RSI_test':new_name}, inplace = True)
        
            # add the RSI test column to the main_df
            main_df = pd.merge(main_df, data, how='outer', on=['Date'])

        # Add an exception for when there are symbols on the list without available data
        except KeyError:
            failed_downloads.append(symbol)
            print(f"No data for {symbol}")

    # Select only the columns starting from the third column
    # Get the distribution of values in each row
    dist_df = main_df.iloc[:, 2:].apply(lambda x: x.value_counts(normalize=True), axis=1)

    # add the RSI test column to the main_df
    main_df = pd.concat([main_df, dist_df], axis=1)

    # Remove RSI_test columns
    close_col = f'{etf}_Close'
    main_df = main_df[['Date', close_col, 'Y', 'N']]

    # print a list of failed downloads
    if failed_downloads:
        print("\nList of failed downloads:")
        for name in failed_downloads:
            print(name)
    else:
        print("No Failed Downloads\n")
    
    main_df.dropna(inplace=True)
    return main_df