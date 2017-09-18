# coin_list.py

import json
import requests

from .helper_functions import build_url, load_data

def get_coin_list(coins='all'):
	"""
	Get general information about all the coins available on 
	cryptocompare.com.
	
	Args:
		coins: Default value of 'all' returns information about all the coins
			available on the site. Otherwise a single string or list of coin 
			symbols can be used.

	Returns:
		The function returns a dictionairy containing individual dictionairies 
		for the coins specified by the input. The key of the top dictionary 
		corresponds to the coin symbol. Each coin dictionary has the following 
		structure:
		
			{coin_symbol1: {'Algorithm' : ...,
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
				    'Url': ...},
	 		coin_symbol2: {...},
 			...}
	"""
	
	# convert single coins input to single element lists
	if not isinstance(coins, list) and coins != 'all':
		coins = [coins]

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
		The function returns a dictionairy containing blockain as well as 
		trading information from the different exchanges were the specified 
		currency pair is available.

		{'AggregatedData': dict,
 		 'Algorithm': ...,
		 'BlockNumber': ...,
		 'BlockReward': ...,
		 'Exchanges': [dict1, dict2, ...],
		 'NetHashesPerSecond': ...,
		 'ProofType': ...,
		 'TotalCoinsMined': ...}

		dict = {'FLAGS': ...,
		        'FROMSYMBOL': ...,
		        'HIGH24HOUR': ...,
		        'LASTMARKET': ...,
		        'LASTTRADEID': ...,
		        'LASTUPDATE': ...,
		        'LASTVOLUME': ...,
		        'LASTVOLUMETO': ...,
		        'LOW24HOUR': ...,
		        'MARKET': ...,
		        'OPEN24HOUR': ...,
		        'PRICE': ...,
		        'TOSYMBOL': ...,
		        'TYPE': ...,
		        'VOLUME24HOUR': ...,
		        'VOLUME24HOURTO': ...}
	"""

	# load data
	url = build_url('coinsnapshot', fsym=fsym, tsym=tsym)
	data = load_data(url)['Data']

	return data