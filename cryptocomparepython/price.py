# price.py

from helper_functions import build_url, load_data, timestamp_to_date


def get_current_price(fsyms, tsyms, e='all', try_conversion=True, full=False, 
                     format='raw'):
	"""Get latest full or compact price information in display or raw format for 
	the specified FROM-TO currency pairs.

	Args:
		fsyms: Single string or list of FROM symbols.
		tsyms: Single string or list of TO symbols.
		e: Default returns average price across all exchanges. Can be set to the
			name of a single exchange. CCAGG = Cryptocompare Aggregate
		full: Default of False returns only the latest price. True returns the 
			following dictionary structure containing the full trading info:
		format: Default returns the 'RAW' format. Can be set to 'DISPLAY' 
			format.
	Returns:
		Returns a dictionary containing the latest price pairs if full is set to
		false:
		
		{fsym1: {tsym1: ..., tsym2:..., ...},
		 fsym2: {...},
		 ...}

		or full trading info dictionaries for all the price pairs in the other
		case:

		{fsym1: {tsym1: {'CHANGE24HOUR': ...,
		 				 'CHANGEPCT24HOUR': ...,
 	                     'FLAGS': ...,
				 	     'FROMSYMBOL': ...,
					 	 'HIGH24HOUR': ...,
					 	 'LASTMARKET': ...,
					 	 'LASTTRADEID': ...,
					 	 'LASTUPDATE': ..., 
					 	 'LASTVOLUME': ...,
					 	 'LASTVOLUMETO': ...,
					 	 'LOW24HOUR': ...,
					 	 'MARKET' ...,
						 'MKTCAP': ...,
						 'OPEN24HOUR': ...,
						 'PRICE': ...,
					 	 'SUPPLY': ...,
					 	 'TOSYMBOL': ...,
					 	 'TYPE': ..., 
					 	 'VOLUME24HOUR': ...,
					 	 'VOLUME24HOURTO': ...},
				 tsym2: ..., ...},
		fsym2: {...},
		...}
	"""

	# select API function based on 'full' parameter value
	if not full:
		func = 'pricemulti'
	else:
		func = 'pricemultifull'

	# convert single fsym and tsym input to single element lists
	if not isinstance(fsyms, list):
		fsyms = [fsyms]
	if not isinstance(tsyms, list):
		tsyms = [tsyms]

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


def get_current_trading_info(fsym, tsym, markets='all', try_conversion=True, 
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
	
	# load data 
	url = build_url('generateAvg', fsym=fsym, tsym=tsym, markets=markets,
	                try_conversion=try_conversion)
	data = load_data(url)

	# select format to return
	if format == 'raw':
		data = data['RAW']
	elif format == 'display':
		data = data['DISPLAY']

	return data


def get_day_average_price(fsym, tsym, e='all', try_conversion=True, 
                    	  avg_type='HourVWAP', utc_hour_diff=0):
	"""
	Get the day average price of a currency pair.

	Args:
		fsym: FROM symbol.
		tsym: TO symbol.
		e: Default returns average price across all exchanges. Can be set to the
			name of a single exchange.
		avg_type: 'HourVWAP' returns a volume weighted average of the hourly
			close price. The other option 'MidHighLow' gives the average between
			the 24 hour high and low.
		utc_hour_diff: Pass hour difference to UTC for different time zone.

		# add 'toTs' parameter
		#
		#
		#
	
	Returns:
		Day average price as float.
	"""

	# load data
	url = build_url('dayAvg', fsym=fsym, tsym=tsym, e=e, 
	                try_conversion=try_conversion, avg_type=avg_type, 
	                utc_hour_diff=utc_hour_diff)
	data = load_data(url)

	# remove 'ConversionType' information
	del data['ConversionType']
	
	return data[tsym]


def get_historical_eod_price(fsym, tsyms, ts, e='all', try_conversion=True):
	"""Get end of day price for cryptocurrency based on the requested timestamp.

	Args:
		fsym: FROM symbol.
		tsyms: Single string or list of TO symbols.
		ts: Unix timestamp.
		e:
		try_conversion: 

	Returns:

	"""

	# convert single fsym and tsym input to single element lists
	if not isinstance(tsyms, list):
		tsyms = [tsyms]

	# load data
	url = build_url("pricehistorical", fsym=fsym, tsyms=tsyms, ts=ts, 
	                e=e, try_conversion=try_conversion)
	data = load_data(url)

	return data


def get_historical_minute_price(fsym, tsym, price='full', e='all', 
                                try_conversion=True, aggregate=1, limit=1440, 
                                to_ts=False):
	"""Get minute historical price and volumne information about the requested
	currency pair. Available data is limited to the last 7 days.
	

	Args:
		fsym: FROM symbol.
		tsym: TO symbol.
		price: Select price or volume information to return. Default of 'full'
			returns all of them.
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

	# load data
	url = build_url('histominute', fsym=fsym, tsym=tsym, e=e, 
	                try_conversion=try_conversion, aggregate=aggregate, 
	                limit=limit, to_ts=to_ts)
	data = load_data(url)
	price_data = data['Data']

	# convert timestamps to nice date format
	for p in price_data:
		p['time'] = timestamp_to_date(p['time'])

	# set return information
	if price == 'full':
		return price_data
	else:
		return [{'time': p['time'], price: p[price]} for p in price_data]

def get_historical_hour_price(fsym, tsym, e='all', try_conversion=True,
                              aggregate=1, limit=168, to_ts=False):
	"""Get hour historical price and volumne information about the requested
	currency pair.
	
	Args:
		fsym: FROM symbol.
		tsym: TO symbol.
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

	# load data
	url = build_url('histohour', fsym=fsym, tsym=tsym, e=e, 
	                try_conversion=try_conversion, aggregate=aggregate, 
	                limit=limit, to_ts=to_ts)
	data = load_data(url)
	price_data = data['Data']

	# convert timestamps to nice date format
	for p in price_data:
		p['time'] = timestamp_to_date(p['time'])

	# set return information
	if price == 'full':
		return price_data
	else:
		return [{'time': p['time'], price: p[price]} for p in price_data]


def get_historical_day_price(fsym, tsym, e='all', try_conversion=True, 
							 aggregate=1, limit=30, to_ts=False):
	"""Get day historical price and volumne information about the requested
	currency pair.
	
	Args:
		fsym: FROM symbol.
		tsym: TO symbol.
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

	# load data
	url = build_url('histoday', fsym=fsym, tsym=tsym, e=e, 
	                try_conversion=try_conversion, aggregate=aggregate, 
	                limit=limit, to_ts=to_ts)
	data = load_data(url)
	price_data = data['Data']
	
	# convert timestamps to nice date format
	for p in price_data:
		p['time'] = timestamp_to_date(p['time'])

	# set return information
	if price == 'full':
		return price_data
	else:
		return [{'time': p['time'], price: p[price]} for p in price_data]


if __name__ == "__main__":

	# print("Examples get_latest_price()")
	# print("--------------------------------")
	# print(get_latest_price("BTC", ["EUR", "USD", "ETH"]))
	# print()

	# print(get_latest_price(["ETH", "BTC"], ["USD"]))
	# print()

	# print(get_latest_price("ETH", ["EUR"], e="Kraken"))
	# print()

	# print(get_latest_price(["ETH", "BTC", "DASH"], ["EUR", "USD"]))
	# print()

	# print(get_latest_price("ETH", ["EUR", "BTC"], full=True))
	# print()

	# print(get_latest_price("ETH", ["EUR", "BTC"], full=True, format="display"))
	# print()

	# print("Examples get_current_trading_info()")
	# print("--------------------------------")
	# print(get_current_trading_info("ETC", "USD"))
	# print()

	# print(get_current_trading_info("BTC", "USD", markets=["Poloniex"]))
	# print()

	# print(get_current_trading_info("BTC", "USD", 
	#                          	   markets=["Poloniex", "Kraken", "Coinbase"], 
	#                                format='display'))
	# print()

	# print("Examples get_day_average_price")
	# print("--------------------------------")
	# print(type(get_day_average_price("ETH", "EUR")))
	# print()

	# print(get_day_average_price("DGB", "XLM", avg_type="MidHighLow", utc_hour_diff=-8))
	# print()

	print("Examples get_historical_eod_price()")
	print("--------------------------------")
	print(get_historical_eod_price("BTC", ["EUR", "USD", "ETH"], ts=1452680400))
	print()

	print(get_historical_eod_price("DASH", "USD", ts=1492689600))
	print()

	print(get_historical_eod_price("LTC", ["BTC", "EUR"], ts=1500768000, 
	                           e="Kraken"))
	print()

	print(get_historical_eod_price("LTC", ["BTC", "EUR"], ts=1500768000, 
	                           e="Coinbase"))
	print()

	# print("Examples get_historical_minute_price()")
	# print("--------------------------------")
	# #print(
	# price_data = get_historical_minute_price('BTC', 'USD', aggregate=5, 
	#                                          limit=100)

	#for p in price_data:
	#	print(timestamp_to_date(p['time']), p['high'])
	#print()

	# print(price_data)
	# print()

	# price_data = get_historical_minute_price('BTC', 'USD', price='open')
	# print(price_data)
	# print()

	# print("Examples get_historical_minute_price()")
	# print("--------------------------------")
	# price_data = get_historical_hour_price('ETH', 'EUR')

	# for p in price_data:
	# 	print(timestamp_to_date(p['time']), p['high'])
	# print()

	# price_data = get_historical_hour_price('ETH', 'EUR', limit=2000)

	# for p in price_data:
	# 	print(timestamp_to_date(p['time']), p['high'])
	# print()