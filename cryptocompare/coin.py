# coin_list.py

import json
import requests

from helper_functions import build_url, load_data

def get_coin_list(coins='all'):
	"""
	Get general information about all the coins available on 
	cryptocompare.com.
	
	Args:
		coins: Default value of 'all' returns complete list. Otherwise a list of 
			coin symbols can be used.

	Returns:
		The function returns a dictionairy containing individual dictionairies 
		for the coins specified by the input. The key of the top dictionary 
		corresponds to the coin symbol. Each coin dictionary has the following 
		structure:
			{'Algorithm' : ...,
			 'CoinName': ...,
			 'FullName': ...,
			 'FullyPremined': ...,
			 'Id': ...,
			 'ImageUrl': ...,
			 'Name': ...,
			 'PreMinedValue': ...,
			 'ProofType': ...,
			 'SortOrder': ...,
			 'TotalCoinsFreeFloat': ...,
			 'TotalCoinSupply': ...,
			 'Url': ...}
	"""
	
	# load data
	url = build_url('coinlist')
	data = load_data(url)['Data']

	# coins specified
	if coins != 'all':
		data = {c: data[c] for c in coins}

	return data


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

	print("Examples get_coin_list()")
	print("--------------------------------")

	# example 1
	coin_data = get_coin_list(coins=["BTC", "ETH"])
	print(coin_data)
	print()

	# example 2
	coin_data = get_coin_list()
	print(list(coin_data.keys())[:10])
	print()

	print("Examples get_coin_snapshot()")
	print("--------------------------------")
	print(get_coin_snapshot("LTC", "EUR"))
	print()