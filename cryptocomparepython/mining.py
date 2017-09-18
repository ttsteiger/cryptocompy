# mining.py

from helper_functions import build_url, load_data


def get_mining_equipment():
	"""Get all the mining equipment available on the Cryptocompare website.

	Returns:


	"""
	url = build_url('miningequipment')
	data = load_data(url)

	print(url)
	return data['MiningData']

if __name__ == "__main__":
	print("Example get_mining_equipment()")
	print("--------------------------------")
	print(get_mining_equipment())


