# import needed modules
import statsmodels.api as sm
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# how cash dividends affect price level
ticker = "AAPL"
start_date = "2020-08-01"
end_date = "2020-08-31"

prices=pdr.get_data_yahoo(ticker, start_date, end_date)

# 