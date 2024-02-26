# import the stock_info submodule from the yahoo_fin module 
from yahoo_fin import stock_info as si #

# start an infinite loop
while True:  #
    # obtain ticker symbol from you
    ticker = input("What's the ticker symbol of the stock you are looking for?\n")  #
    # if you want to stop, type in "done"
    if ticker =="done":   #
        break
    # otherwise, type in a stock ticker symbol
    else:
        try:
            # obtain live stock price from Yahoo
            price = si.get_live_price(ticker)
            # print out the stock price
            print(f"the stock price for {ticker} is {round(price,2)}")
        except:
            print("invalid ticker symbol")

    
