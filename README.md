# cryptocompare-python
Simple wrapper for the CryptoCompare API.

https://www.cryptocompare.com/api/#-api-data-price-

To do:
- add tryConversion parameter
- wrap url build into function
- mamke oo approach? base object with build_url, add_to_url, get_data methods

## Functions

#### get_coin_information(coins='all')

#### get_latest_price(fsyms, tsyms, e='all', full=False, format='raw')

#### get_latest_average(fsym, tsym, markets, format='raw')

#### get_day_average(fsym, tsym, e='all', avgType='HourVWAP', UTCHourDiff=0)
