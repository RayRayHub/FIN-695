# Define Imports
import requests

def FirmByTicker(ticker):
    try:
        # Extract the source code from the website
        url = 'https://query1.finance.yahoo.com/v1/finance/search?q='+ticker
        response = requests.get(url, headers={'User-Agent':'...','referer':'https://...'})
        # Read the JSON data
        response_json = response.json()
        # Obtain the value corresponding to "quotes"
        quotes = response_json['quotes']
        # Get the ticker symbol
        firm = quotes[0]['shortname']
        # Print out the ticker
        return firm
    except:
        print("Sorry, not a valid ticker entry!")

def TickerByFirm(firm):
    try:
        # Extract the source code from the website
        url = 'https://query1.finance.yahoo.com/v1/finance/search?q='+firm
        response = requests.get(url, headers={'User-Agent':'...','referer':'https://...'})
        # Read the JSON data
        response_json = response.json()
        # Obtain the value corresponding to "quotes"
        quotes = response_json['quotes']
        # Get the ticker symbol
        ticker = quotes[0]['symbol']
        # Print out the ticker
        return ticker
    except:
        print("Sorry, not a valid firm entry!")