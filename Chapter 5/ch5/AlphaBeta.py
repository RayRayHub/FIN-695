# import needed modules
import statsmodels.api as sm
from pandas_datareader import data as pdr
import yfinance as yfin
yfin.pdr_override()

# set the start and end dates
start_date = "2020-12-01"
end_date = "2021-05-31"
# choose market index (S&P500) and stock ticker symbols
market = "^GSPC" 
ticker = input("what's the ticker?")
sp = pdr.get_data_yahoo( market, start=start_date, end=end_date)
stock = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)
print(sp)
print(stock)
#calculate returns for sp500 and the stock
sp['ret_sp'] =(sp['Adj Close']/sp['Adj Close'].shift(1))-1
stock['ret_stock'] =(stock['Adj Close']/stock['Adj Close'].shift(1))-1
# merge the two datasets, keep only returns
df = sp[['ret_sp']].merge(stock[['ret_stock']], left_index=True, right_index=True) 
#add risk free rate (assume constant for simplicity) 
df['rf'] = 0.00001
# we need a constant to run regressions
df['const'] = 1 
df['exret_stock'] = df.ret_stock - df.rf
df['exret_sp'] = df.ret_sp - df.rf
# remove missing values
df.dropna(inplace=True) 
# Calculate the stock's alpha and Beta
reg = sm.OLS(endog=df['exret_stock'], exog=df[['const', 'exret_sp']], missing='drop')
results = reg.fit()
print(results.summary())
alpha=round(results.params['const']*100,3)
beta=round(results.params['exret_sp'],2)
# print the values of alpha and beta
print(f'the alpha of the stock {ticker} is {alpha} percent')
print(f'the beta of the stock {ticker} is {beta}')



