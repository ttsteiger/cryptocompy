# get_price_historical.py
import json
import requests


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
	base_url = "https://min-api.cryptocompare.com/data/pricehistorical?"
	fsym_url = "fsym={}".format(fsym)
	tsyms_url = "tsyms={}".format(",".join(tsyms))
	ts_url = "ts={}".format(ts)

	url = "{}{}&{}&{}".format(base_url, fsym_url, tsyms_url, ts_url)

	# exchange specified
	if e != 'all':
		e_url = "e={}".format(e)
		url = "{}&{}".format(url, e_url)

	# http request
	r = requests.get(url)

	# decode to json
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