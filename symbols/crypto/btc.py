import requests
import pandas as pd

def get_btc_data(days=30):
    """
    Fetch BTC price data from CoinGecko API.

    :param days: Number of days of historical data to fetch (default: 30)
    :return: DataFrame with date and price
    """
    url = f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days={days}&interval=daily"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        prices = data['prices']

        df = pd.DataFrame(prices, columns=['timestamp', 'price'])
        df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
        df = df[['date', 'price']]

        return df

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()

def btc():
    return get_btc_data()