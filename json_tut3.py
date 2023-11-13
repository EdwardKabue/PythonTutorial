import json
from urllib.request import urlopen

#get json response from API
with urlopen("https://query1.finance.yahoo.com/v8/finance/chart/aapl?metrics=high?&interval=1d&range=5d") as response:
    source = response.read()

data = json.loads(source)

print(json.dumps(data, indent=2))

currency = ""
usymbol = ""

for item in data["chart"]["result"]:
    if type(item) is dict:
        for x in item:
            if x == "meta":
                currency = item[x]["currency"]
                usymbol = item[x]["symbol"]

print(f"Currency: {currency}, Symbol: {usymbol}")