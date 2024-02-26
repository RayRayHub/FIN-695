# import needed modules
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# set the start and end dates
start_date = "2022-02-01"
end_date = "2023-01-31"
# obtain stock price
ticker = "TSLA"  #
stock = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)
#calculate returns 
stock['ret_stock'] =stock['Adj Close'].pct_change()  #
#calculate moving averages
avg_trading_days = 21
stock['avg1m']=stock['ret_stock'].rolling(avg_trading_days).mean()  #
stock['avg2m']=stock['ret_stock'].rolling(avg_trading_days*2).mean()   
stock['avg6m']=stock['ret_stock'].rolling(avg_trading_days*6).mean()
#calculate squared forecast errors
stock['err1m']=stock['ret_stock']-stock['avg1m'].shift(1) #
stock['sqerr1m']=stock['err1m']*stock['err1m']  #
stock['err2m']=stock['ret_stock']-stock['avg2m'].shift(1)
stock['sqerr2m']=stock['err2m']*stock['err2m']
stock['err6m']=stock['ret_stock']-stock['avg6m'].shift(1)
stock['sqerr6m']=stock['err6m']*stock['err6m']
stock = stock.dropna() 

#calcualte avearage squared error for each method
stock.dropna(inplace=True) 
print('the squared error using 1-month moving average is', stock['sqerr1m'].mean())  #
print('the squared error using 3-month moving average is', stock['sqerr2m'].mean())
print('the squared error using 6-month moving average is', stock['sqerr6m'].mean())

