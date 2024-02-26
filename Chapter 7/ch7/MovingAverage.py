# import needed modules
from pandas_datareader import data as pdr

# set the start and end dates
start_date = "2021-02-01"   #
end_date = "2021-08-31"
# obtain stock price
ticker = "IBM"
stock = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)
#calculate returns 
stock['ret_stock'] = (stock['Adj Close']/stock['Adj Close'].shift(1))-1 #
#calculate moving averages
stock.dropna(inplace=True) 
stock['avg6m']=stock['ret_stock'].rolling(126).mean()  # 

# Use Aug 23 avg6m value to predict return on Aug 24
forecast_ret=stock['ret_stock']["2021-08-23"]
print("the predicted return on Aug 24 is", forecast_ret)
# Find out the stock price on Aug 23
price_today=stock['Adj Close']["2021-08-23"]
print("the price on Aug 23 is", price_today)
# Predict tomorrow's price
pred=price_today*(1+forecast_ret)
print("the predicted price on Aug 24 is", pred) 
