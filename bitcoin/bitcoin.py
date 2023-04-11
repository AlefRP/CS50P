import json
import sys
import requests

# Main function
def main():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    btc = sys.argv[1]
    btcprice = get_bitcoin_price()
    try:
        amount = float(btc) * btcprice
        print(f"${amount:,.4f}")
    except ValueError:
        sys.exit("Command-line argument is not a number")

# Get today's bitcoin price with requests
def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit()
    data = json.loads(response.text)
    usd_rate_float = data['bpi']['USD']['rate_float']
    return usd_rate_float

# Call main
main()
