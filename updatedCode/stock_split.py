import yfinance
yfinance.pdr_override()
from pandas_datareader import data as pdr
import pandas as pd

# set the start and end dates
start = "2020-08-16"
end = "2020-08-31"
ticker = "AAPL"
stock = pdr.get_data_yahoo(ticker,
               start=start, end=end)
pd.options.display.float_format = "{:,.2f}".format   
print(stock)










