import yfinance as yf
import pandas as pd

def usd_myr():
    """
    Fetch Forex data for the USD/MYR currency pair using Yahoo Finance.

    :return: DataFrame with date and price
    """
    try:
        # Set the Forex pair for USD to MYR
        pair = "MYR=X"  # USD/MYR pair on Yahoo Finance is represented as MYR=X

        # Fetch historical data for the USD/MYR pair
        ticker = yf.Ticker(pair)
        data = ticker.history(period="1mo")  # Fetching 1 month of data

        # Reset index to get 'date' from the index
        df = data.reset_index()[['Date', 'Close']]
        df.columns = ['date', 'price']  # Renaming columns for consistency

        return df

    except Exception as e:
        print(f"Error fetching Forex data for USD/MYR: {e}")
        return pd.DataFrame()
