# cryptocompare-python
Simple wrapper for the public CryptoCompare API.

https://www.cryptocompare.com/api

To do:
- add all get functions
- complete docstrings
- create readme with examples
- error handling for http requests
- throw warnings for conversions


## Functions

#### coin.py
* get_coin_list(coins='all')
* get_coin_snapshot(fsym, tsym)

#### price.py
* get_current_price(fsyms, tsyms, e='all', try_conversion=True, full=False, format='raw')
* get_current_trading_info(fsym, tsym, markets='all', try_conversion=True, format='raw)
* get_day_average_price(fsym, tsym, e='all', try_conversion=True, avg_type='HourVWAP, utc_hour_diff=0)
* get_historical_eod_price(fsym, tsyms, ts, e='all', try_conversion=True)
* get_historical_minute_price(fsym, tsym, price='full', e='all', try_conversion=True, aggregate=1, limit=1440, to_ts=False)
* get_historical_hour_price(fsym, tsym, e='all', try_conversion=True, aggregate=1, limit=168, to_ts=False)
* get_historical_day_price(fsym, tsym, e='all', try_conversion=True, aggregate=1, limit=30, to_ts=False)

#### mining.py
* get_mining_equipment()

#### rest.py
* AllExchanges() (unfinished)

#### top.py
* get_top_exchanges_by_volume(fsym, tsym, limit=5)
* get_top_coins_by_volume(tsym, limit=20)
* get_top_pairs_by_volume(fsym, limit=5)