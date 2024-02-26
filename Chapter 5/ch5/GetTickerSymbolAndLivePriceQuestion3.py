import TickerFirmProvider as tfp
from yahoo_fin import stock_info as si #

# Start an infinite loop
while True:
    # Obtain company name from you
    firm = input("Which company's ticker/stock price are you looking for?\n")
    # If you want to stop, type in "done"
    if firm == "done":
        break
    # Otherwise, type in a company name
    else:
        try:
            # Get the ticker symbol
            ticker = tfp.TickerByFirm(firm)
            # obtain live stock price from Yahoo
            price = si.get_live_price(ticker)
            # Print out the ticker and stock price
            print(f"The ticker symbol for {firm} is {ticker}. The stock price is {round(price,2)}")
        except:
            print("Sorry, not a valid entry!")
        continue