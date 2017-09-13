# price.py

import json
import requests

from helper_functions import build_url, load_data, timestamp_to_date


def get_latest_price(fsyms, tsyms, e='all', try_conversion=True, full=False, 
                     format='raw'):
	"""
	Get latest full or compact price information in display or raw format for 
	the specified FROM-TO currency pairs.

	Args:
		fsyms: List of FROM symbols.


		# allow list or single value for input
		#
		#


		tsyms: List of TO symbols.
		e: Default returns average price across all exchanges. Can be set to the
			name of a single exchange. CCAGG = Cryptocompare Aggregate
		full: Default of False returns only the latest price. True returns the 
			following dictionary structure containing the full :
				{'TYPE': ..., 
			 	 'LASTVOLUME': ..., 
			 	 'CHANGE24HOUR': ..., 
			 	 'LASTUPDATE': ...,, 
			 	 'OPEN24HOUR': ..., 
			 	 'MKTCAP': ...,
			 	 'FLAGS': ...,
			 	 'LASTVOLUMETO': ...,
			 	 'VOLUME24HOURTO': ...,
			 	 'LASTTRADEID': ...,
			 	 'FROMSYMBOL': ...,
			 	 'SUPPLY': ...,
			 	 'CHANGEPCT24HOUR': ...,
			 	 'TOSYMBOL': ...,
			 	 'LOW24HOUR': ...,
			 	 'VOLUME24HOUR': ...,
			 	 'HIGH24HOUR': ...,
			 	 'LASTMARKET': ...,
			 	 'PRICE': ...,
			 	 'MARKET' ...}
		format: Default returns the 'RAW' format. Can be set to 'DISPLAY' 
			format.
	Returns:
		Returns a dictionary containing the latest price pairs...



	"""

	# select API function based on 'full' parameter value
	if not full:
		func = 'pricemulti'
	else:
		func = 'pricemultifull'

	# load data
	url = build_url(func, fsyms=fsyms, tsyms=tsyms, e=e, 
	                try_conversion=try_conversion)
	data = load_data(url)

	#  select right format to return for full requests
	if full and format == 'raw':
		data = data['RAW']
	elif full and format == 'display':
		data = data['DISPLAY']

	return data


def get_latest_average(fsym, tsym, markets='all', try_conversion=True, 
                       format='raw'):
	"""
	Get the latest trading info of the requested pair as a volume weighted 
	average based on the markets requested.
	
	Args:
		fsym: FROM symbol.
		tsym: TO symbol.
		markets: List containing the market names. 
		format: Default returns the 'RAW' format. Can be set to 'DISPLAY' 
			format.

	Returns:
		The returned latest average trading information dictionary contains
		the following key value pairs:
		
		{'PRICE': ...,
		 'LASTVOLUMETO': ...,
		 'TOSYMBOL': ...,
		 'LOW24HOUR': ...,
		 'CHANGE24HOUR': ...,
		 'FROMSYMBOL': ...,
		 'FLAGS': ...,
		 'VOLUME24HOUR': ...,
		 'HIGH24HOUR': ...,
		 'LASTUPDATE': ...,
		 'VOLUME24HOURT': ...,
		 'LASTMARKET': ...,
		 'CHANGEPCT24HOUR': ...,
		 'OPEN24HOUR': ...,
		 'MARKET': ...,
		 'LASTTRADEID': ...,
		 'LASTVOLUME': ...}
	"""
	
	# build url 
	url = build_url('generateAvg', fsym=fsym, tsym=tsym, markets=markets,
	                try_conversion=try_conversion)

	# http request
	r = requests.get(url)

	# decode to json
	data = r.json()

	if format == 'raw':
		data = data['RAW']
	elif format == 'display':
		data = data['DISPLAY']

	return data


def get_day_average(fsym, tsym, e='all', try_conversion=True, 
                    avgType='HourVWAP', UTCHourDiff=0):
	"""
	Get the day average price of a currency pair.

	Args:
		fsym: FROM symbol.
		tsym: TO symbol.
		e: Default returns average price across all exchanges. Can be set to the
			name of a single exchange.
		avgType: 'HourVWAP' returns a volume weighted average of the hourly
			close price. The other option 'MidHighLow' gives the average between
			the 24 hour high and low.
		UTCHourdiff: 

		# add 'toTs' parameter
		#
		#
		#
	
	Returns:
		'ConversionType' information
		...


	"""

	# build url
	url = build_url('dayAvg', fsym=fsym, tsym=tsym, e=e, 
	                try_conversion=try_conversion, avgType=avgType, 
	                UTCHourDiff=UTCHourDiff)

	# http request
	r = requests.get(url)

	# decode to json
	data = r.json()

	# remove 'ConversionType' information
	#del data['ConversionType']
	
	return {fsym: data}


def get_historical_eod_price(fsym, tsyms, ts, markets='all', try_conversion=True):
	"""Get end of day price for cryptocurrency based on the requested timestamp.

	Args:
		fsym: From symbol.
		tsyms: List of TO symbols.
		ts: Unix timestamp.
		markets:
		try_conversion: 

	Returns:

	"""

	# load data
	url = build_url("pricehistorical", fsym=fsym, tsyms=tsyms, ts=ts, 
	                markets=markets, try_conversion=try_conversion)
	data = load_data(url)

	return data


def get_historical_minute_price(fsym, tsym, e='all', try_conversion=True,
                                aggregate=1, limit=1440, to_ts=False):
	"""Get minute historical price and volumne information about the requested
	currency pair. Available data is limited to the last 7 days.
	

	Args:
		fsym: From symbol.
		tsym: To symbol.
		e: Default returns average price across all exchanges. Can be set to the
		   name of a single exchange. CCCAGG = Cryptocompare Aggregate
		tryConversion:
		aggregate: Aggregates the minute prices into bins of the specified size.
		limit: Number of minute prices. The default value of 1440 is equal to 24 
			hoursMaximum value of 2000. Using aggregate reduces the number of 
			points returned by a factor equal to the chosen bin size.
		to_ts: ????
	
	Returns:
		List of dictionairies containing the price and volume information for
		each requested tick.

		[{'time': ..., 'close': ..., 'high': ..., 'low': ..., 'open': ...,
		  'volumefrom': ..., 'volumeto': ...},
		  {...},
		  ...]
	"""
	url = build_url('histominute', fsym=fsym, tsym=tsym, e=e, 
	                try_conversion=try_conversion, aggregate=aggregate, 
	                limit=limit, to_ts=to_ts)
	data = load_data(url)

	return data['Data']


def get_historical_hour_price(fsym, tsym, e='all', try_conversion=True,
                              aggregate=1, limit=168, to_ts=False):
	"""Get hour historical price and volumne information about the requested
	currency pair.
	
	Args:
		fsym: From symbol.
		tsym: To symbol.
		e: Default returns average price across all exchanges. Can be set to the
		   name of a single exchange. CCCAGG = Cryptocompare Aggregate
		try_conversion:
		aggregate: Aggregates the hour prices into bins of the specified size.
		limit: 168h = 7d, max 2000
		to_ts: ????

	Returns:
		List of dictionairies containing the price and volume information for
		each requested tick.

		[{'time': ..., 'close': ..., 'high': ..., 'low': ..., 'open': ...,
		  'volumefrom': ..., 'volumeto': ...},
		  {...},
		  ...]
	"""
	url = build_url('histohour', fsym=fsym, tsym=tsym, e=e, 
	                try_conversion=try_conversion, aggregate=aggregate, 
	                limit=limit, to_ts=to_ts)
	data = load_data(url)

	return data['Data']


def get_historical_day_price():
	"""Get day historical price and volumne information about the requested
	currency pair.
	
	Args:
		fsym: From symbol.
		tsym: To symbol.
		e: Default returns average price across all exchanges. Can be set to the
		   name of a single exchange. CCCAGG = Cryptocompare Aggregate
		try_conversion:
		aggregate: max 30
		limit: 30d = 1m, max 2000
		to_ts: ????

	Returns:
		List of dictionairies containing the price and volume information for
		each requested tick.

		[{'time': ..., 'close': ..., 'high': ..., 'low': ..., 'open': ...,
		  'volumefrom': ..., 'volumeto': ...},
		  {...},
		  ...]
	"""
	url = build_url('histoday', fsym=fsym, tsym=tsym, e=e, 
	                try_conversion=try_conversion, aggregate=aggregate, 
	                limit=limit, to_ts=to_ts)
	data = load_data(url)

	return data['Data']


if __name__ == "__main__":

	# print("Examples get_latest_price()")
	# print("--------------------------------")
	
	# print(get_latest_price(["BTC"], ["EUR", "USD", "ETH"]))
	# print()

	# print(get_latest_price(["ETH"], ["EUR"], e="Kraken"))
	# print()

	# print(get_latest_price(["ETH", "BTC", "DASH"], ["EUR", "USD"]))
	# print()

	# print(get_latest_price(["ETH"], ["EUR", "BTC"], full=True))
	# print()

	# print(get_latest_price(["ETH"], ["EUR", "BTC"], full=True, format="display"))
	# print()

	# print("Examples get_latest_average()")
	# print("--------------------------------")
	# print(get_latest_average("BTC", "USD", markets=["Poloniex"]))
	# print()

	# print(get_latest_average("BTC", "USD", 
	#                          markets=["Poloniex", "Kraken", "Coinbase"], 
	#                          format='display'))
	# print()

	# print("Examples get_day_average")
	# print("--------------------------------")
	# print(get_day_average("ETH", "EUR"))
	# print()

	# print(get_day_average("DGB", "XLM", avgType="MidHighLow", UTCHourDiff=-8))
	# print()

	# print("Examples get_historical_eod_price()")
	# print("--------------------------------")
	# print(get_historical_eod_price("BTC", ["EUR", "USD", "ETH"], ts=1452680400))
	# print()

	# print(get_historical_eod_price("DASH", ["USD"], ts=1492689600))
	# print()

	# print(get_historical_eod_price("LTC", ["BTC", "EUR"], ts=1500768000, 
	#                            markets=["Kraken"]))
	# print()

	print("Examples get_historical_minute_price()")
	print("--------------------------------")
	#print(
	price_data = get_historical_minute_price('BTC', 'USD', aggregate=5, 
	                                         limit=300)

	for p in price_data:
		print(timestamp_to_date(p['time']), p['high'])
	print()

	print("Examples get_historical_minute_price()")
	print("--------------------------------")
	price_data = get_historical_hour_price('ETH', 'EUR')

	for p in price_data:
		print(timestamp_to_date(p['time']), p['high'])
	print()

	price_data = get_historical_hour_price('ETH', 'EUR', limit=2000)

	for p in price_data:
		print(timestamp_to_date(p['time']), p['high'])
	print()