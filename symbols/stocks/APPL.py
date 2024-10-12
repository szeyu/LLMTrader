import yfinance as yf
import pandas as pd

def appl():
    """
    Fetch AAPL stock price data using Yahoo Finance.

    :return: DataFrame with date and price
    """
    try:
        # Fetch historical data for AAPL stock
        ticker = yf.Ticker("AAPL")
        data = ticker.history(period="1mo")  # Fetching 1 month of data

        # Reset index to get 'date' from the index
        df = data.reset_index()[['Date', 'Close']]
        df.columns = ['date', 'price']  # Renaming columns for consistency

        return df

    except Exception as e:
        print(f"Error fetching AAPL data: {e}")
        return pd.DataFrame()
