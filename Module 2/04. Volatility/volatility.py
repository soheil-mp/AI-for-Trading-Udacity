import pandas as pd
import numpy as np

def get_most_volatile(prices):
    """Return the ticker symbol for the most volatile stock.
    
    Parameters
    ----------
    prices : pandas.DataFrame
        a pandas.DataFrame object with columns: ['ticker', 'date', 'price']
    
    Returns
    -------
    ticker : string
        ticker symbol for the most volatile stock
    """
    # Set the "date" column as index
    prices = prices.set_index('date')
    
    # Initialize an empty list
    hv_list = []
    
    # Loop over the ticker symbols
    for i_ticker in prices.ticker.unique():
        
        # Get the prices of given ticker
        ticker_prices = prices[prices['ticker'] == i_ticker]['price'] 
        
        # 
        ticker_lret = np.log(ticker_prices / ticker_prices.shift(1))
        
        # Calculate the standard deviation
        ticker_hv = ticker_lret.std() 
        
        # Append the result to the list
        hv_list.append(ticker_hv) 
        
    # Convert list to series
    hv_Series = pd.Series(hv_list)
    
    # Set the ticker names as index
    hv_Series.index = prices.ticker.unique()
    
    # Get the most volatile stock name
    ticker = hv_Series.idxmax()
   
    return ticker


def test_run(filename = './prices.csv'):
    """Test run get_most_volatile() with stock prices from a file."""
    prices = pd.read_csv(filename, parse_dates=['date'])
    print("Most volatile stock: {}".format(get_most_volatile(prices)))


if __name__ == '__main__':
    test_run()
