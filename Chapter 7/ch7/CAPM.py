# import needed modules
import statsmodels.api as sm
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# set the start and end dates
start_date = "2019-12-25"
end_date = "2020-06-25"

# choose market index (S&P500) and stock ticker symbols
market = "^GSPC" 
ticker = "AAPL"

sp = pdr.get_data_yahoo(market, start=start_date, end=end_date)
stock = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)

#calculate returns for sp500 and the stock
sp['ret_sp'] = (sp['Adj Close']/sp['Adj Close'].shift(1))-1
stock['ret_stock'] = (stock['Adj Close']/stock['Adj Close'].shift(1))-1

# merge the two datasets, keep only returns
df = sp[['ret_sp']].merge(stock[['ret_stock']], left_index=True, right_index=True) 

# we need a constant to run regressions
df['const'] = 1 

# remove missing values
df.dropna(inplace=True) 

# Calculate the stock's alpha and Beta
reg = sm.OLS(endog=df['ret_stock'], exog=df[['const', 'ret_sp']], missing='drop')

results = reg.fit()

print(results.params)

print(results.params["ret_sp"])

alpha = results.params["const"]

beta = results.params["ret_sp"]

#calculate the expected market return
mkt_ret = df['ret_sp'].mean()

# forecast
expected_ret = alpha + beta * mkt_ret

print('the forecast for Apple stock return on June 26, 2020, is', expected_ret)

# next day price = today's price * (1 + expected_ret)

price_today = stock["Adj Close"]["2020-06-25"]

print(price_today)


