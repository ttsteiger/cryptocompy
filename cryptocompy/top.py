# top.py

from .helper_functions import build_url, load_data

def get_top_exchanges(fsym, tsym, limit=5):
	"""Get top exchanges by 24 hour trading volume for the currency pair.
	
	Args:
		fsym: FROM symbol.
		tsym: TO symbol.
		limit: Number of results. Default value returns top 5 exchanges.

	Returns:
		Function returns a list containing a dictionary for each result:

		[{'exchange': ..., 'fromSymbol': ..., 'toSymbole': ..., 
		  'volume24h': ..., 'volume24hTo': ...}, 
		 {...}, 
		 ...]

		The list is ordered based on the volume of the FROM currency starting 
		with the highest value.
	"""

	# load data
	url = build_url('exchanges', fsym=fsym, tsym=tsym, limit=limit)
	data = load_data(url)

	# price_data = data['Data']
	# return [{'exchange': p['exchange'],
	#		  'volume24hto': p['volume24hTo']} for p in price_data]

	return data['Data']

def get_top_coins(tsym, limit=20):
	"""Get top coins by 24 hour trading volume value in the requested currency.
	
	Args:
		tsym: TO symbol.
		limit: Number of results. Default value returns top 20 coins.
	
	Returns:
		Function returns a list containing a dictionary for each result:

		[{'SUPPLY': ..., 'SYMBOL': ..., 'VOLUME24HOURTO': ...}, 
		 {...}, 
		 ...]

		The list is ordered based on the volume of the TO currency starting with 
		the highest value.
	"""
	
	# load data
	url = build_url('volumes', tsym=tsym, limit=limit)
	data = load_data(url)

	return data['Data']


def get_top_pairs(fsym, limit=5):
	"""Get top trading pairs by 24 hour aggregated volume for a currency.
	
	Args:
		fsym: FROM symbol.
		limit: Number of results. Default value returns top 5 pairs.
	
	Returns:
		Function returns a list containing a dictionary for each result:

		[{'exchange': ..., 'fromSymbol': ..., 'toSymbol': ..., 'volume24h': ..., 
		  'volume24hTo': ...}, 
 		 {...}, 
 		 ...]

		The list is ordered based on the volume of the FROM currency starting 
		with the highest value.
	"""

	# load data
	url = build_url('pairs', fsym=fsym, limit=limit)
	data = load_data(url)

	return data['Data']

