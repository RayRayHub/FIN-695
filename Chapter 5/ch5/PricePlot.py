#import needed modules
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import matplotlib.dates as mdates
import yfinance as yfin
yfin.pdr_override()

#set the start and end date
start_date = "2021-02-25" 
end_date = "2021-08-25"

#choose stock ticker symbol
ticker = "TSLA"
#get stock price
stock = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)
print(stock)
#obtain dates
stock['Date']=stock.index.map(mdates.date2num)
#choose figure size
fig = plt.figure(dpi=128, figsize=(10, 6))
#format date to place on the x-axis
formatter = mdates.DateFormatter('%m/%d/%Y')
plt.gca().xaxis.set_major_formatter(formatter)
# Plot data.
plt.plot(stock['Date'], stock['Adj Close'], c='blue')
# Format plot.
plt.title("The Stock Price", fontsize=16)
plt.xlabel('Date', fontsize=10)
fig.autofmt_xdate()
plt.ylabel("Price", fontsize=10)
plt.show()


