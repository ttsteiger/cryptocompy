# helper_functions.py

import datetime
import json
import requests


def build_url(func, **kwargs):
	"""
	"""

	if func in ['coinlist', 'coinsnapshot']:
		url = "https://www.cryptocompare.com/api/data/{}?".format(func)
	else:
		url = "https://min-api.cryptocompare.com/data/{}?".format(func)
	
	# collect url parts in list
	url_parts = []

	for key, value in kwargs.items():
		if key == 'fsym':
			url_parts.append("fsym={}".format(value))
		elif key == 'fsyms':
			url_parts.append("fsyms={}".format(",".join(value)))
		elif key == 'tsym':
			url_parts.append("tsym={}".format(value))
		elif key == 'tsyms':
			url_parts.append("tsyms={}".format(",".join(value)))
		
		# exchange
		elif key == 'e' and value != 'all':
			url_parts.append("e={}".format(value))
		elif key == 'e' and value == 'all':
			url_parts.append("e={}".format('CCCAGG'))
		
		# conversion
		elif key == 'try_conversion' and not value:
			url_parts.append("tryConversion=false")
		
		elif key == 'markets' and value != 'all':
			url_parts.append("markets={}".format(",".join(value)))
		elif key == 'avgType' and value != 'HourVWAP':
			url_parts.append("avgType={}".format(value))
		elif key == 'UTCHourDiff' and value != 0:
			url_parts.append("UTCHourDiff={}".format(value))
		elif key == 'ts':
			url_parts.append("ts={}".format(value))
		elif key == 'aggregate' and value != 1:
			url_parts.append("aggregate={}".format(value))
		elif key == 'limit' and value != 1440:
			url_parts.append("limit={}".format(value))

	# put url together
	url = url + "&".join(url_parts)

	return url


def load_data(url):
	"""
	"""

	# http request
	r = requests.get(url)

	# decode to json
	data = r.json()

	return data


def timestamp_to_date(ts):
		"""Convert timestamp to nice date and time format.

		Args:
			ts: Timestamp as string.

		Returns:
			
		"""
		return datetime.datetime.fromtimestamp(int(ts)
		                                       ).strftime('%Y-%m-%d %H:%M:%S')