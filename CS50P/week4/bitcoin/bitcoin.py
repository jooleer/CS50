import sys
import requests
import json

# json file with current BTC price
btc_json = "https://api.coindesk.com/v1/bpi/currentprice.json"

if __name__ == "__main__":
    # check for correct amount of arguments
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    # reject input that does not use a dot as a decimal separator
    amount = sys.argv[1]
    if not amount.replace('.', '', 1).isnumeric():
        sys.exit("Command-line argument is not a number")

    # attempt to retreive btc_json
    try:
        response = requests.get(btc_json)
    except requests.RequestException:
        sys.exit("Request Error")

    # fetch json data
    o = response.json()
    price = o["bpi"]["USD"]["rate"]

    # calculate, format and print value
    split_price = price.split(",")
    price = split_price[0] + split_price[1]
    value = float(price) * float(amount)
    format_value = "{:,.4f}".format(value)
    print("$" + str(format_value))
