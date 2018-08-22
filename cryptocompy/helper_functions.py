# helper_functions.py

import datetime
import json
import requests
import time


def build_url(func, **kwargs):
	"""
	"""

	if func in ['coinlist', 'coinsnapshot', 'miningcontracts', 
				'miningequipment']:
		url = "https://www.cryptocompare.com/api/data/{}?".format(func)
	elif func in ['exchanges', 'volumes', 'pairs']:
		url = "https://min-api.cryptocompare.com/data/top/{}?".format(func)
	elif func in ['minute', 'hour', 'day']:
		url = "https://min-api.cryptocompare.com/data/histo{}?".format(func)
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
		
		# markets
		elif key == 'markets' and value != 'all':
			url_parts.append("e={}".format(",".join(value)))
		elif key == 'markets' and value == 'all':
			url_parts.append("e={}".format('CCCAGG'))

		elif key == 'avg_type' and value != 'HourVWAP':
			url_parts.append("avgType={}".format(value))
		elif key == 'utc_hour_diff' and value != 0:
			url_parts.append("UTCHourDiff={}".format(value))
		elif key == 'to_ts':
			url_parts.append("toTs={}".format(value))
		elif key == 'aggregate' and value != 1:
			url_parts.append("aggregate={}".format(value))
		
		elif key == 'limit':
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


def date_to_timestamp(date):
	"""
	

	Args:
		date: Date as string with these formats: "Y-m-d", "Y-m-d H-M-S".
	Returns:
	
	"""
	
	# format input string if only date but no time is provided
	if len(date) == 10:
		date = "{} 00:00:00".format(date)

	return time.mktime(time.strptime(date, '%Y-%m-%d %H:%M:%S')) # 




if __name__ == "__main__":
	date = timestamp_to_date('1492689600')
	ts = date_to_timestamp(date)

	print(date, ts)
