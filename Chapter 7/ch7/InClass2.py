# want predict y
# assume y=a+b*x
# run regression to estimate a and b
# when forecasting y=a+b*x

# predict stock returm
# r = a + b * mkt

# import needed modules
import statsmodels.api as sm
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# forecast AMZN return
market = "^GSPC"
ticker = "AMZN"
start_date = "2022-01-01"
end_date = "2023-02-28"

price=pdr.get_data_yahoo(ticker, start_date, end_date)
market=pdr.get_data_yahoo(market, start_date, end_date)

# Calculate returns for sp500 and the stock
price["ret"]=price["Adj Close"].pct_change()
market["mkt"]=market["Adj Close"].pct_change()

# merge the two datasets, keep only returns
df = price[['ret']].merge(market[['mkt']], left_index=True, right_index=True)

# we need a constant to run regressions
df['const'] = 1

# remove missing values
df.dropna(inplace=True)

# Calculate the stock's alpha and Beta
reg = sm.OLS(df['ret'], df[['const', 'mkt']], missing='drop')

result = reg.fit()

print(result.params)

alpha=result.params['const']
beta=result.params['mkt']

# Calculate the expected market return
mkt_ret = df['mkt'].mean()

# Forecast
expected_ret=alpha+beta*mkt_ret
print('the forecast for Apple stock return on February 28, 2023, is', expected_ret)