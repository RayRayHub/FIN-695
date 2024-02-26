# import needed modules
from pandas_datareader import data as pdr

# set the start and end dates
start_date = "2019-07-01"
end_date = "2020-06-30"
# obtain stock price
ticker = "TSLA"  #
stock = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)
#calculate returns 
stock['ret_stock'] =(stock['Adj Close']/stock['Adj Close'].shift(1))-1  #
#calculate moving averages
stock.dropna(inplace=True) 
stock['avg1m']=stock['ret_stock'].rolling(21).mean()  #
stock['avg3m']=stock['ret_stock'].rolling(63).mean()   
stock['avg6m']=stock['ret_stock'].rolling(126).mean()
#calculate squared forecast errors
stock['err1m']=stock['ret_stock']-stock['avg1m'].shift(1) #
stock['sqerr1m']=stock['err1m']*stock['err1m']  #
stock['err3m']=stock['ret_stock']-stock['avg3m'].shift(1)
stock['sqerr3m']=stock['err3m']*stock['err3m']
stock['err6m']=stock['ret_stock']-stock['avg6m'].shift(1)
stock['sqerr6m']=stock['err6m']*stock['err6m']
#calcualte avearage squared error for each method
stock.dropna(inplace=True) 
print('the squared error using 1-month moving average is', stock['sqerr1m'].mean())  #
print('the squared error using 3-month moving average is', stock['sqerr3m'].mean())
print('the squared error using 6-month moving average is', stock['sqerr6m'].mean())

