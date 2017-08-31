# coin_snapshot.py

from helper_functions import build_url, load_data

def get_coin_snapshot(fsym, tsym):
	"""
	Get blockchain information, aggregated data as well as data for the 
	individual exchanges available for the specified currency pair.

	Args:
		fsym: FROM symbol.
		tsym: TO symbol.
	
	Returns:
		'ConversionType' information
	"""

	# load data
	url = build_url('coinsnapshot', fsym=fsym, tsym=tsym)
	data = load_data(url)['Data']

	print(url)

	return data

if __name__ == "__main__":

	print("Examples get_coin_snapshot()")
	print("--------------------------------")
	print(get_coin_snapshot("LTC", "EUR"))
	print()