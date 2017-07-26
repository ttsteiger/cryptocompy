# get_historical.py
import json
import requests

from helper_functions import build_url

def get_histo(scale, fsym, tsym, e='all', aggregate=1, limit=30):
	"""
	...

	Args:
		fsym:
		tsym:
		e:
		aggregate:
		limit:



	Returns:
	...

	"""

	# selected scale determines func
	if scale == 'day':
		func = 'histoday'
	elif scale == 'hour':
		func = 'histohour'
	elif scale == 'minute':
		func = 'histominute'

	# build url
	url = build_url(func, fsym=fsym, tsym=tsym, e=e, aggregate=aggregate,
	                limit=limit)
	
	# http request
	r = requests.get(url)

	# decode to json 
	data = r.json()

	return data['Data']


if __name__ == "__main__":
	
	data = get_histo("day", "ETH", "EUR")
	print(data)
	print()

	print(len(data))
