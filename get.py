# get.py
import json
import requests


def get_coin_information(coins='all'):
	"""
	Return general information about all the coins available on 
	cryptocompare.com.
	
	Args:
		coins: Default of 'all' returns complete list. Otherwise a list of coin
			symbols can be used.

	Returns:
		The function returns a dictionairy containing containing dictionairies
		for the coins specified by the input. The key of the top dictionary
		corresponds to the coin symbol. Each coin dictionary contains the 
		following key and value pairs:
			'Algorithm' 
			'CoinName'
			'FullName'
			'FullyPremined'
			'Id'
			'ImageUrl'
			'Name'
			'PreMinedValue'
			'ProofType'
			'SortOrder'
			'TotalCoinsFreeFloat'
			'TotalCoinSupply'
			'Url'
	"""
	
	# http request
	url = "https://www.cryptocompare.com/api/data/coinlist/"
	r = requests.get(url)

	# data extraction
	data = r.json()
	response = data["Response"]
	message = data["Message"]
	coin_data = data["Data"]

	print(message)

	# coins specified
	if coins != 'all':
		coin_data = {c: coin_data[c] for c in coins}

	return coin_data


def get_



if __name__ == "__main__":

	# examples get_coin_information()
	coin_data = get_coin_information(["BTC", "ETH"])
	print(coin_data)

	coin_data = get_coin_information()
	print(list(coin_data.keys())[:10])

	# examples
