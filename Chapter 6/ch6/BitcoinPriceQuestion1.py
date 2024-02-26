import requests
import html

# specify the url to find the bitcoin price
url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
#get the live information from bitcoin url
response = requests.get(url)
# read the JSON data
response_json = response.json()
# obtain the GBP dictionary
gbp=response_json['bpi']['GBP']
# get the price
price=gbp['rate']
# get the html entity
symbol=gbp['symbol']
print(f"The Bitcoin price as a {type(price)} is {html.unescape(symbol)}{price}.")