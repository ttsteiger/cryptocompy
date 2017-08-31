# cryptocompare-python
Simple wrapper for the CryptoCompare API.

https://www.cryptocompare.com/api

To do:
- add all get functions
- complete docstrings
- create readme with examples



## Functions

#### coin_list.py
* get_coin_list(coins='all')

#### price.py
* get_latest_price(fsyms, tsyms, e='all', try_conversion=True, full=False, format='raw')
* get_latest_average(fsym, tsym, markets='all', try_conversion=True, format='raw')
* get_day_average(fsym, tsym, e='all', try_conversion=True, avgType='HourVWAP', UTCHourDiff=0)

#### price_historical.py
* get_price_historical(fsym, tsyms, ts, markets='all', try_conversion=True)

#### coin_snapshot.py
* get_coin_snapshot()
