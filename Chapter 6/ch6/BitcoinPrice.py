import requests

# specify the url to find the bitcoin price
url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
#get the live information from bitcoin url
response = requests.get(url)
# read the JSON data
response_json = response.json()
# obtain the USD dictionary
usd=response_json['bpi']['USD']
# get the price
price=usd['rate_float']
print(f"The Bitcoin price is ${price}.")



