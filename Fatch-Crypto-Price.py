import requests

symbols = ["BTCUSDT", 'ETHUSDT', 'SOLUSDT', 'XRPUSDT']
url = "https://api.binance.com/api/v3/ticker/price"

for symbol in symbols:
    response = requests.get(url, params ={"symbol" : symbol})
    if response.status_code == 200:
        data = response.json()
        print(f"Symbol : {data['symbol']}, Price : {data['price']}")
    else:
        print(f"Error Fetching{symbol} : {response.status_code}")