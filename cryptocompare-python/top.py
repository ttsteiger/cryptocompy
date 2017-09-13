# top.py

from helper_functions import build_url, load_data

def get_top_exchanges_by_volume(fsym, tsym, limit=5):
	"""Get top exchanges by trading volume for the currency pair.
	
	Args:
		fsym: FROM symbol.
		tsym: TO symbol.
		limit:

	Returns:

	"""

	# load data
	url = build_url('exchanges', fsym=fsym, tsym=tsym, limit=limit)
	data = load_data(url)
	price_data = data['Data']

	return [{'exchange': p['exchange'],
			 'volume24hto': p['volume24hTo']} for p in price_data]

def get_top_coins_by_volume(tsym, limit=20):
	"""Get top coins by trading volume value in the requested currency.
	
	Args:
		tsym: TO symbol.
		limit:
	
	Returns:

	"""
	
	# load data
	url = build_url('volumes', tsym=tsym, limit=limit)
	data = load_data(url)


	return data['Data']


def get_top_pairs_by_volume(fsym, limit=5):
	"""Get top pairs by aggregated trading volume for a currency.
	
	Args:
		fsym: FROM symbol.
		limit:
	
	Returns:

	"""

	# load data
	url = build_url('pairs', fsym=fsym, limit=limit)
	data = load_data(url)


	return data['Data']


if __name__ == "__main__":

	# print("Examples get_top_exchanges_by_volume()")
	# print("--------------------------------")
	# print(get_top_exchanges_by_volume('BTC', 'EUR'))
	# print()

	print("Examples get_top_coins_by_volume()")
	print("--------------------------------")
	print(get_top_coins_by_volume('EUR', limit=5))
	print()

	# print("Examples get_top_pairs_by_volume()")
	# print("--------------------------------")
	# print(get_top_pairs_by_volume('EUR'))
	# print()