import MetaTrader5 as mt5
import pandas as pd
import pytz
from datetime import datetime

def download_candles(symbol, timeframe, start_date, end_date):
    # Connect to MetaTrader 5
    if not mt5.initialize():
        print("initialize() failed, error code =", mt5.last_error())
        return None
    
    # Set time zone to UTC
    #mt5.set_timezone(mt5.TIMEZONE_UTC)
    
    # Define request parameters
    request_params = {
        "symbol": symbol,
        "timeframe": timeframe,
        "start_date": start_date,
        "end_date": end_date
    }
    
    # Request historical data
    candles = mt5.copy_rates_range(symbol, timeframe, start_date, end_date)
    
    # Disconnect from MetaTrader 5
    mt5.shutdown()
    
    return candles

def save_to_csv(candles, filename):
    # Convert candles data to DataFrame
    df = pd.DataFrame(candles)
    
    # Save DataFrame to CSV
    df.to_csv(filename, index=False)
    print("Data saved to", filename)

if __name__ == "__main__":
    # Define parameters
    symbol = "XAUUSD"  # Gold
    timeframe = mt5.TIMEFRAME_M15  # M15 timeframe
    timezone = pytz.timezone("Etc/UTC")
    start_date =  datetime(2023, 1, 1, tzinfo=timezone) # Start date for historical data
    end_date = datetime(2024, 4, 2, tzinfo=timezone) # End date for historical data
    filename = "XAUUSD_M15.csv"  # Output CSV filename
    
    # Download candles
    candles = download_candles(symbol, timeframe, start_date, end_date)
    if candles is not None:
        # Save candles to CSV
        save_to_csv(candles, filename)