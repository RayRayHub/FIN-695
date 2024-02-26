from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()


start="2022-08-01"
end="2023-01-31"

ticker="IBM"

stock = pdr.get_data_yahoo(ticker, start=start, end=end)

#calculate returns
stock['ret_stock'] = (stock['Adj Close'].pct_change())
stock['oldret'] = stock['Adj Close']/stock['Adj Close'].shift(1)-1

#moving average
stock["avg1mth"]=stock["ret_stock"].rolling(21).mean()
stock["avg2mth"]=stock["ret_stock"].rolling(42).mean()

#imagine you are standing at Jan 31,2023
#predict IBM ret on Feb 2
forecast_ret=stock["avg2mth"]["2023-01-30"]
print("The predicted return on Feb 2nd is", forecast_ret)

#Convert return into price
current_price = stock["Adj Close"]["2023-01-30"]

#forecast next day IBM price
next_day_price=current_price*(1+forecast_ret)
print("the predicted price on Aug 24 is", next_day_price)