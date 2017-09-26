# mining.py

from .helper_functions import build_url, load_data


def get_mining_contracts():
	"""
 	Get all the mining contracts information available.

 	Returns:
 		This function returns two major dictionaries. The first one contains 
 		information about the coins for which mining contracts data is 
 		available: 

		coin_data: 


			{symbol1: {'BlockNumber': ...,
			           'BlockReward': ...,
			           'BlockRewardReduction': ...,
			           'BlockTime': ...,
			           'DifficultyAdjustment': ...,
			           'NetHashesPerSecond': ...,
			           'PreviousTotalCoinsMined': ...,
			           'PriceUSD': ...,
			           'Symbol': ...,
			           'TotalCoinsMined': ...},
 			 symbol2: {...},
 			 ...}

		The other one contains all the available mining contracts:

		mining_data: 

			{id1: {'AffiliateURL': ...,
			       'Algorithm': ...,
			       'Company': ...,
			       'ContractLength': ...,
			       'Cost': ...,
			       'CurrenciesAvailable': ...,
			       'CurrenciesAvailableLogo': ...,
			       'CurrenciesAvailableName': ...,
			       'Currency': ...,
			       'FeePercentage': ...,
			       'FeeValue': ...,
			       'FeeValueCurrency': ...,
			       'HashesPerSecond': ...,
			       'Id': id1,
			       'LogoUrl': ...,
			       'Name': ...,
			       'ParentId': ...,
			       'Recommended': ...,
			       'Sponsored': ...,
			       'Url': ...},
			 id2: {...},
			 ...} 
	"""

	# load data
	url = build_url('miningcontracts')
	data = load_data(url)
	coin_data = data['CoinData']
	mining_data = data['MiningData']

	return coin_data, mining_data


def get_mining_equipment():
	"""Get all the mining equipment information available.

	Returns:
		This function returns two major dictionaries. The first one contains information about the coins for which mining equipment data is available.

		coin_data: 

			{symbol1: {'BlockNumber': ...,
			           'BlockReward': ...,
			           'BlockRewardReduction': ...,
			           'BlockTime': ...,
			           'DifficultyAdjustment': ...,
			           'NetHashesPerSecond': ...,
			           'PreviousTotalCoinsMined': ...,
			           'PriceUSD': ...,
			           'Symbol': ...,
			           'TotalCoinsMined': ...},
			 symbol2: {...},
			 ...}

		The other one contains all the available mining equipment.

		mining_data:

			{id1: {'AffiliateURL': ...,
			       'Algorithm': ...,
			       'Company': ...,
			       'Cost': ...,
			       'CurrenciesAvailable': ...,
			       'CurrenciesAvailableLogo': ...,
			       'CurrenciesAvailableName': ...,
			       'Currency': ...,
			       'EquipmentType': ...,
			       'HashesPerSecond': ...,
			       'Id': ...,
			       'LogoUrl': ...,
			       'Name': ...,
			       'ParentId': ...,
			       'PowerConsumption': ...,
			       'Recommended': ...,
			       'Sponsored': ...,
			       'Url': ...},
			 id2: {...},
	"""

	# load data
	url = build_url('miningequipment')
	data = load_data(url)
	coin_data = data['CoinData']
	mining_data = data['MiningData']

	return coin_data, mining_data