# import needed modules
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# set the start and end dates
start_date = "2022-10-01"
end_date = "2023-01-31"
# obtain stock price
ticker = "KR"
stock = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)
#calculate returns 
stock['ret_stock'] = (stock['Adj Close'].pct_change())
#calculate moving averages
stock.dropna(inplace=True) 
stock['avg3m']=stock['ret_stock'].rolling(21*3).mean()
# forecast the stock price of Kroger on Feb 2, 2023, 
# based on the moving average in the previous three months.
forecast_ret=stock['ret_stock']["2023-01-30"]
print("the predicted return on Jan 30 is", forecast_ret)
# Find out the stock price on Jan 30
price_today=stock['Adj Close']["2023-01-30"]
print("the price on Jan 30 is", price_today)
# Predict tomorrow's price
pred=price_today*(1+forecast_ret)
print("the predicted price on Feb 2 is", pred) 

start_date = "2023-02-01"
end_date = "2023-02-02"
stock = pdr.get_data_yahoo(ticker, start_date, end_date)
print("the actual price on Feb 2 was", stock['Adj Close']["2023-02-01"])
