import sys
import requests
import json

btc_json = "https://api.coindesk.com/v1/bpi/currentprice.json"

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

amount = sys.argv[1]
if not amount.replace('.', '', 1).isnumeric():
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get(btc_json)
except requests.RequestException:
    sys.exit("Request Error")


o = response.json()
price = o["bpi"]["USD"]["rate"]

split_price = price.split(",")
price = split_price[0] + split_price[1]
value = float(price) * float(amount)
format_value = "{:,.4f}".format(value)
print("$" + str(format_value))
