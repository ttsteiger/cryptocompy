# get_price_historical.py
import json
import requests

from helper_functions import build_url

def get_price_historical(fsym, tsyms, ts, e='all'):
	"""
	
	Get end of day price for the specified timestamp.

	Args:
		fsym: From symbol.
		tsyms: List of TO symbols.
		ts: Unix timestamp.

	Returns:

	"""

	# build url
	url = build_url("pricehistorical", fsym=fsym, tsyms=tsyms, ts=ts, e=e)

	print(url)

	# # http request
	r = requests.get(url)

	# # decode to json
	data = r.json()

	return data

if __name__ == "__main__":

	print("Examples get_price_historical()")
	print("--------------------------------")
	print(get_price_historical("BTC", ["EUR", "USD", "ETH"], ts=1452680400))
	print()

	print(get_price_historical("DASH", ["USD"], ts=1492689600))
	print()

	print(get_price_historical("LTC", ["BTC", "EUR"], ts=1500768000, e="Kraken"))
	print()