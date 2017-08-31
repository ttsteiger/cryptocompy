# get_price_historical.py

from helper_functions import build_url, load_data

def get_price_historical(fsym, tsyms, ts, markets='all', try_conversion=True):
	"""
	
	Get end of day price for the specified timestamp.

	Args:
		fsym: From symbol.
		tsyms: List of TO symbols.
		ts: Unix timestamp.

	Returns:

	"""

	# load data
	url = build_url("pricehistorical", fsym=fsym, tsyms=tsyms, ts=ts, 
	                markets=markets, try_conversion=try_conversion)
	data = load_data(url)

	return data

if __name__ == "__main__":

	print("Examples get_price_historical()")
	print("--------------------------------")
	print(get_price_historical("BTC", ["EUR", "USD", "ETH"], ts=1452680400))
	print()

	print(get_price_historical("DASH", ["USD"], ts=1492689600))
	print()

	print(get_price_historical("LTC", ["BTC", "EUR"], ts=1500768000, 
	                           markets=["Kraken"]))
	print()