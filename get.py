# get.py
import json
import requests


def get_coinlist():
	"""
	Return general information about all the coins available on 
	cryptocompare.com. The function returns a dictionary with its keys being 
	the coin symbols and the values being dictionaries containing information
	about the specified coin.

	The following parameters will be returned for each coin:

	'Algorithm'            - 
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

	return coin_data

if __name__ == "__main__":
	coin_data = get_coinlist()

	print(len(coin_data.keys()))
	print(coin_data["BTC"])