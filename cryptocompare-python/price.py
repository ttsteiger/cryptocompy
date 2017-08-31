# price.py

import json
import requests

from helper_functions import build_url, load_data

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


if __name__ == "__main__":

	print("Examples get_latest_price()")
	print("--------------------------------")
	
	# 
	print(get_latest_price(["BTC"], ["EUR", "USD", "ETH"]))
	print()

	print(get_latest_price(["ETH"], ["EUR"], e="Kraken"))
	print()

	print(get_latest_price(["ETH", "BTC", "DASH"], ["EUR", "USD"]))
	print()

	print(get_latest_price(["ETH"], ["EUR", "BTC"], full=True))
	print()

	print(get_latest_price(["ETH"], ["EUR", "BTC"], full=True, format="display"))
	print()

	print("Examples get_latest_average()")
	print("--------------------------------")
	print(get_latest_average("BTC", "USD", markets=["Poloniex"]))
	print()

	print(get_latest_average("BTC", "USD", 
	                         markets=["Poloniex", "Kraken", "Coinbase"], 
	                         format='display'))
	print()

	print("Examples get_day_average")
	print("--------------------------------")
	print(get_day_average("ETH", "EUR"))
	print()

	print(get_day_average("DGB", "XLM", avgType="MidHighLow", UTCHourDiff=-8))
	print()