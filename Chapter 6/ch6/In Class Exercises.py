import requests

link="https://api.coindesk.com/v1/bpi/currentprice.json"

prices = requests.get(link)

print(prices.text)

prices_json = prices.json()

for k,v in prices_json.items():
    print(k)
    print(v)

usd=prices_json['bpi']

print(usd)

bitcoin_usd=usd['USD']

print(bitcoin_usd)

price=bitcoin_usd['rate_float']
print(f"The Bitcoin price is ${price}.")
