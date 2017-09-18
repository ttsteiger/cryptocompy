
# cryptocomparepython
Simple wrapper for the public CryptoCompare API.

Cryptocompare API:
https://www.cryptocompare.com/api

## Table of Contents

* [ToDo](#ToDo)
* [Installation](#Installation)
* [Code of Conduct](#code-of-conduct)
* [Contributing](#Contributing)
* [Documentation](#Documentation)
    * [coin.py](#coinpy)
        * [get_coin_list](#get_coin_list)
        * [get_coin_snapshot](#get_coin_snapshot)
    * [price.py](#pricepy)
        * [get_current_price](#get_current_price)
        * [get_current_trading_info](#get_current_trading_info)
        * [get_day_average_price](#get_day_average_price)
		* [get_historical_eod_price](#get_historical_eod_price)
		* [get_historical_data](get_historical_data#)
    * [mining.py](#mining.py)
    * [top.py](#top.py)

## ToDo:

- add all get functions
- complete docstrings
- create readme with examples
- error handling for http requests
- throw warnings for conversions
- add toTs parameter to price functions

## Installation

dsfsdfdsfsdfds
sdfsdfdfsdfsdfsdf
sdfsdfdsfsdfsdfsdf
sfsdfsdfdsfffsdfsdf
fdsdfsdfsdfds

## Code of Conduct

Dont abuse wrapper to spam the Cryptocompare API. A request every 10 seconds should be more than enough.

## Contributing

If you would like to help me with my work or have any suggestions for improvements please follow the "fork-and-pull" Git workflow.

1. Fork the repo on GitHub
2. Clone the project to your own machine
3. Commit changes to your own branch
4. Push your work back up to your fork
5. Submit a Pull request so that we can review your changes

NOTE: Be sure to merge the latest from "upstream" before making a pull request!


## Documentation

### coin.py

#### get_coin_list

```python
get_coin_list(coins='all')
```

Get general information about all the coins available on cryptocompare.com.

*Arguments:*

`coins`: Default value of `'all'` returns information about all the coins available on the site. Otherwise a single string or list of coin symbols can be used.

*Returns:*

The function returns a dictionairy containing individual dictionairies for the coins specified by the input. The key of the top dictionary corresponds to the coin symbol. The dictionary returned has the following structure:

```
{coin_symbol1: {'Algorithm' : ...,
                'CoinName': ...,
                'FullName': ...,
                'FullyPremined': ...,
                'Id': ...,
                'ImageUrl': ...,
                'Name': ...,
                'PreMinedValue': ...,
                'ProofType': ...,
                'SortOrder': ...,
                'TotalCoinsFreeFloat': ...,
                'TotalCoinSupply': ...,
			    'Url': ...},
 coin_symbol2: {...},
 ...}
```

*Example 1:*

Get general coin information for Bitcoin and Ethereum.


```python
from cryptocomparepython import coin

coin_data = coin.get_coin_list(coins=["BTC", "ETH"])
coin_data
```




    {'BTC': {'Algorithm': 'SHA256',
      'CoinName': 'Bitcoin',
      'FullName': 'Bitcoin (BTC)',
      'FullyPremined': '0',
      'Id': '1182',
      'ImageUrl': '/media/19633/btc.png',
      'Name': 'BTC',
      'PreMinedValue': 'N/A',
      'ProofType': 'PoW',
      'SortOrder': '1',
      'TotalCoinSupply': '21000000',
      'TotalCoinsFreeFloat': 'N/A',
      'Url': '/coins/btc/overview'},
     'ETH': {'Algorithm': 'Ethash',
      'CoinName': 'Ethereum ',
      'FullName': 'Ethereum  (ETH)',
      'FullyPremined': '0',
      'Id': '7605',
      'ImageUrl': '/media/20646/eth.png',
      'Name': 'ETH',
      'PreMinedValue': 'N/A',
      'ProofType': 'PoW',
      'SortOrder': '2',
      'TotalCoinSupply': '0',
      'TotalCoinsFreeFloat': 'N/A',
      'Url': '/coins/eth/overview'}}



*Example 2:*

Return information for all the coins available on Cryptocompare and print out ten of their symbols.


```python
coin_data = coin.get_coin_list()
coin_symbols = list(coin_data.keys())[:10]
coin_symbols
```




    ['BAT',
     'WEALTH',
     'GML',
     'PLANET',
     'CACH',
     'STEEM',
     'DCR',
     'CRAB',
     'CCC',
     'NVST']



---

#### get_coin_snapshot

```python
get_coin_snapshot(fsym, tsym)
```

Get blockchain information, aggregated data as well as data for the individual exchanges available for the specified currency pair.

*Arguments:*

* `fsym`: FROM symbol.
* `tsym`: TO symbol. Blockchain information will only be returned if this parameter is a fiat currency.

*Returns:*

The function returns a dictionairy containing blockain as well as trading information from the different exchanges were the specified currency pair is available.

```
{'AggregatedData': dict,
 'Algorithm': ...,
 'BlockNumber': ...,
 'BlockReward': ...,
 'Exchanges': [dict1, dict2, ...],
 'NetHashesPerSecond': ...,
 'ProofType': ...,
 'TotalCoinsMined': ...}
 
dict = {'FLAGS': ...,
        'FROMSYMBOL': ...,
        'HIGH24HOUR': ...,
        'LASTMARKET': ...,
        'LASTTRADEID': ...,
        'LASTUPDATE': ...,
        'LASTVOLUME': ...,
        'LASTVOLUMETO': ...,
        'LOW24HOUR': ...,
        'MARKET': ...,
        'OPEN24HOUR': ...,
        'PRICE': ...,
        'TOSYMBOL': ...,
        'TYPE': ...,
        'VOLUME24HOUR': ...,
        'VOLUME24HOURTO': ...}
```

*Example 1:*

Get all the exchanges were the LTC/EUR currency pair is available for trading.


```python
coin_data = coin.get_coin_snapshot("LTC", "EUR")
exchanges = [e['MARKET'] for e in coin_data['Exchanges']]
exchanges
```




    ['BitSquare',
     'Tidex',
     'HitBTC',
     'Kraken',
     'CCEDK',
     'Yacuna',
     'BTCE',
     'TheRockTrading',
     'Bitstamp',
     'Cexio',
     'Exmo',
     'BitBay',
     'Coinbase']



*Example 2:*

Get the aggregated trading volume across all the available exchanges for the NEO/BTC pair. 


```python
coin_data = coin.get_coin_snapshot("NEO", "BTC")
volume = float(coin_data['AggregatedData']['VOLUME24HOUR'])
volume
```




    639060.1425667896



---

### price.py

#### get_current_price

```python
get_current_price(fsyms, tsyms, e='all', try_conversion=True, full=False, format='raw')
```

Get latest trading price or full trading information in display or raw format for the specified FROM/TO currency pairs.

*Arguments:*

* `fsyms`: Single string or list of FROM symbols.
* `tsyms`: Single string or list of TO symbols.
* `e`: Default returns average price across all exchanges. Can be set to the name of a single exchange.
* `try_conversion`: If the crypto does not trade directly into the toSymbol requested, BTC will be used for conversion. If set to false, it will try to get values without using any conversion at all.
* `full`: Default of False returns only the latest price.	
* `format`: Default returns the 'RAW' format. Can be changed to 'DISPLAY' format.

*Returns:*

Returns a dictionary containing the latest price pairs if full is set to false:

```
{fsym1: {tsym1: ..., tsym2:..., ...},
 fsym2: {...},
 ...}
```

or full trading info dictionaries for all the price pairs in the other case:

```
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
```

*Example 1:*

Get the current BTC prices averaged across all exchanges in EUR, USD and ETH.


```python
from cryptocomparepython import price

price_data = price.get_current_price("BTC", ["EUR", "USD", "ETH"])
price_data
```




    {'BTC': {'ETH': 13.73, 'EUR': 3390.43, 'USD': 4012.43}}



*Example 2:*

Get the current BTC and ETH prices in EUR and USD.


```python
price_data = price.get_current_price(["ETH", "BTC"], ["EUR", "USD"])
price_data
```




    {'BTC': {'EUR': 3390.43, 'USD': 4012.11},
     'ETH': {'EUR': 246.57, 'USD': 292.07}}



*Example 3:*

Get the current ETH trading price in EUR from Kraken. 


```python
price_data = price.get_current_price("ETH", "EUR", e="Kraken")
price_data
```




    {'ETH': {'EUR': 246.61}}



*Example 4:*

Get the current trading information about the ETH/EUR and ETH/BTC markets.


```python
price_data = price.get_current_price("ETH", ["EUR", "BTC"], full=True)
price_data
```




    {'ETH': {'BTC': {'CHANGE24HOUR': 0.002939999999999998,
       'CHANGEPCT24HOUR': 4.207212364052659,
       'FLAGS': '4',
       'FROMSYMBOL': 'ETH',
       'HIGH24HOUR': 0.07574,
       'LASTMARKET': 'Binance',
       'LASTTRADEID': 1136090,
       'LASTUPDATE': 1505764938,
       'LASTVOLUME': 1.236,
       'LASTVOLUMETO': 0.089983272,
       'LOW24HOUR': 0.06949,
       'MARKET': 'CCCAGG',
       'MKTCAP': 6895788.618818946,
       'OPEN24HOUR': 0.06988,
       'PRICE': 0.07282,
       'SUPPLY': 94696355.6553,
       'TOSYMBOL': 'BTC',
       'TYPE': '5',
       'VOLUME24HOUR': 444941.48196087003,
       'VOLUME24HOURTO': 32447.318580023275},
      'EUR': {'CHANGE24HOUR': 26.549999999999983,
       'CHANGEPCT24HOUR': 12.067084810471767,
       'FLAGS': '4',
       'FROMSYMBOL': 'ETH',
       'HIGH24HOUR': 252.75,
       'LASTMARKET': 'Kraken',
       'LASTTRADEID': 1505764916.8202,
       'LASTUPDATE': 1505764916,
       'LASTVOLUME': 0.06129912,
       'LASTVOLUMETO': 15.1169759832,
       'LOW24HOUR': 215.26,
       'MARKET': 'CCCAGG',
       'MKTCAP': 23349280413.927322,
       'OPEN24HOUR': 220.02,
       'PRICE': 246.57,
       'SUPPLY': 94696355.6553,
       'TOSYMBOL': 'EUR',
       'TYPE': '5',
       'VOLUME24HOUR': 170025.47670066005,
       'VOLUME24HOURTO': 40814776.80419911}}}



*Example 5:*

Get the current trading information about the ETH/EUR and ETH/BTC markets in 'DISPLAY' format.


```python
price_data = price.get_current_price("ETH", ["EUR", "BTC"], full=True, format="display")
price_data
```




    {'ETH': {'BTC': {'CHANGE24HOUR': 'Ƀ 0.0029',
       'CHANGEPCT24HOUR': '4.21',
       'FROMSYMBOL': 'Ξ',
       'HIGH24HOUR': 'Ƀ 0.07574',
       'LASTMARKET': 'Binance',
       'LASTTRADEID': 1136090,
       'LASTUPDATE': 'Just now',
       'LASTVOLUME': 'Ξ 1.24',
       'LASTVOLUMETO': 'Ƀ 0.08998',
       'LOW24HOUR': 'Ƀ 0.06949',
       'MARKET': 'CryptoCompare Index',
       'MKTCAP': 'Ƀ 6,895.83 K',
       'OPEN24HOUR': 'Ƀ 0.06988',
       'PRICE': 'Ƀ 0.07282',
       'SUPPLY': 'Ξ 94,696,871',
       'TOSYMBOL': 'Ƀ',
       'VOLUME24HOUR': 'Ξ 444,941.5',
       'VOLUME24HOURTO': 'Ƀ 32,447.3'},
      'EUR': {'CHANGE24HOUR': '€ 26.55',
       'CHANGEPCT24HOUR': '12.07',
       'FROMSYMBOL': 'Ξ',
       'HIGH24HOUR': '€ 252.75',
       'LASTMARKET': 'Kraken',
       'LASTTRADEID': 1505764916.8202,
       'LASTUPDATE': 'Just now',
       'LASTVOLUME': 'Ξ 0.06130',
       'LASTVOLUMETO': '€ 15.12',
       'LOW24HOUR': '€ 215.26',
       'MARKET': 'CryptoCompare Index',
       'MKTCAP': '€ 23.35 B',
       'OPEN24HOUR': '€ 220.02',
       'PRICE': '€ 246.57',
       'SUPPLY': 'Ξ 94,696,871',
       'TOSYMBOL': '€',
       'VOLUME24HOUR': 'Ξ 170,025.5',
       'VOLUME24HOURTO': '€ 40,814,776.8'}}}



---

#### get_current_trading_info

```python
get_current_trading_info(fsym, tsym, markets='all', try_conversion=True, format='raw)
```

Get the latest trading info of the requested pair as a volume weighted average across the markets requested.

*Arguments:*

* `fsym`: FROM symbol.
* `tsym`: TO symbol.
* `markets`: List containing the market names. Default returns average across all markets. If only a single market is specified, the function will also return the full aggregate.
* `try_conversion`: If the crypto does not trade directly into the toSymbol requested, BTC will be used for conversion. If set to false, it will try to get values without using any conversion at all.
* `format`: Default returns the 'RAW' format. Can be set to 'DISPLAY' format.

*Returns:*

The returned latest average trading information dictionary contains the following key value pairs:

```
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
```

*Example 1:*

Get current trading information about the BTC/USD pair across all markets.


```python
price_data = price.get_current_trading_info("BTC", "USD")
price_data
```




    {'BTC': {'USD': {'CHANGE24HOUR': 292.71000000000004,
       'CHANGEPCT24HOUR': 7.869881189556296,
       'FLAGS': 0,
       'FROMSYMBOL': 'BTC',
       'HIGH24HOUR': 4100.52,
       'LASTMARKET': 'CCCAGG',
       'LASTTRADEID': 21078682,
       'LASTUPDATE': 1505764946,
       'LASTVOLUME': 1.49e-05,
       'LASTVOLUMETO': 0.059828566,
       'LOW24HOUR': 3667.71,
       'MARKET': 'CUSTOMAGG',
       'OPEN24HOUR': 3719.37,
       'PRICE': 4012.08,
       'TOSYMBOL': 'USD',
       'VOLUME24HOUR': 136859.14186894277,
       'VOLUME24HOURTO': 539516218.3176087}}}



*Example 2:*

Obtain the trading information aggregated for Poloniex, Kraken and Coinbase in display format.


```python
price_data = price.get_current_trading_info("BTC", "USD", markets=["Poloniex", "Kraken", "Coinbase"], 
                                            format='display')
price_data
```




    {'BTC': {'USD': {'CHANGE24HOUR': '$ 274.53',
       'CHANGEPCT24HOUR': '7.34',
       'FROMSYMBOL': 'Ƀ',
       'HIGH24HOUR': '$ 4,135',
       'LASTMARKET': 'Poloniex',
       'LASTTRADEID': 8712263,
       'LASTUPDATE': 'Just now',
       'LASTVOLUME': 'Ƀ 0.00001020',
       'LASTVOLUMETO': '$ 0.04082',
       'LOW24HOUR': '$ 3,654.74',
       'MARKET': 'CUSTOMAGG',
       'OPEN24HOUR': '$ 3,738.22',
       'PRICE': '$ 4,012.75',
       'TOSYMBOL': '$',
       'VOLUME24HOUR': 'Ƀ 33,194.8',
       'VOLUME24HOURTO': '$ 130,693,784.9'}}}



---

#### get_day_average_price

```python
get_day_average_price(fsym, tsym, e='all', try_conversion=True, avg_type='HourVWAP', utc_hour_diff=0)
```

Get the current days average price of a currency pair.

*Arguments:*

* `fsym`: FROM symbol.
* `tsym`: TO symbol.
* `e`: Default returns average price across all exchanges. Can be set to the name of a single exchange.
* `try_conversion`: If the crypto does not trade directly into the toSymbol requested, BTC will be used for conversion. If set to false, it will try to get values without using any conversion at all.
* `avg_type`: 'HourVWAP' returns a volume weighted average of the hourly close price. The other option 'MidHighLow' gives the average between the 24 hour high and low.
* `utc_hour_diff`: Pass hour difference to UTC for different time zone.

*Returns:*

Returns a price dictionairy containing the current days average price as float.

```
{fsym: {tsym: price}}
```

*Example 1:*

Get the current days ETH/EUR average price across all exchanges.


```python
price_data = price.get_day_average_price("ETH", "EUR")
price_data
```




    {'ETH': {'EUR': 242.6}}



*Example 2:*

Get the MidHighLow price for the DGB/XLM pair in the UTC-8 time zone. 


```python
price_data = price.get_day_average_price("DGB", "XLM", avg_type="MidHighLow", utc_hour_diff=-8)
price_data
```




    {'DGB': {'XLM': 1.13}}



---

#### get_historical_eod_price

```python
get_historical_eod_price(fsym, tsyms, date, e='all', try_conversion=True)
```

Get end of day price for cryptocurrency in any other currency for the requested timestamp.

*Arguments:*

* `fsym`: FROM symbol.
* `tsyms`: Single string or list of TO symbols.
* `date`: Date as string with these formats: "Y-m-d", "Y-m-d H-M-S".Date as string with this format: "Y-m-d H-M-S".
* `e`: Default returns average price across all exchanges. Can be set to the name of a single exchange.
* `try_conversion`: If the crypto does not trade directly into the toSymbol requested, BTC will be used for conversion. If set to false, it will try to get values without using any conversion at all.

*Returns:*

Returns a dictionary containing the end of day price pairs for the provided date.

```
{fsym: {tsym1: ..., tsym2: ..., ...}}
```

*Example 1:*

Get the end of day price from April 20, 2017 for DASH in USD.


```python
price_data = price.get_historical_eod_price("DASH", "USD", "2017-04-20 00:00:00")
price_data
```




    {'DASH': {'USD': 72.34}}



*Example 2:*

Obtain the end of day price of LTC in BTC and EUR from Kraken on the 23rd of July in 2017.


```python
price_data = price.get_historical_eod_price("LTC", ["BTC", "EUR"], "2017-07-23", e="Kraken")
price_data
```




    {'LTC': {'BTC': 0.0165, 'EUR': 40.03}}



---

#### get_historical_data

```python
get_historical_data(fsym, tsym, freq, info='full', e='all', try_conversion=True, aggregate=1, 
                    limit=1440, to_ts=False)
```

Get minute-by-minute historical price and volume information for the requested currency pair. Available data is limited to the last 7 days.

*Arguments:*

* `fsym`: FROM symbol.
* `tsym`: TO symbol.
* `info`: Select price or volume information to return. Default of 'full' returns all of them. Can be set to 'high', 'low', 'open', 'close', 'volumefrom', and 'volumeto' or a list containing several of those values.
* `e`: Default returns average price across all exchanges. Can be set to the name of a single exchange.
* `try_conversion`: If the crypto does not trade directly into the toSymbol requested, BTC will be used for conversion. If set to false, it will try to get values without using any conversion at all.
* `aggregate`: Aggregates the minute prices into bins of the specified size.
* `limit`: Number of minute prices. The limit settings depend on the freq selected. Using aggregate reduces the maximum number of points that can be returned by a factor equal to the chosen bin size.
               minute: default = 1440, min = 1, max = 2000
               hour: default = 168, min = 1, max 2000
               day: default = 30, min = 1, max 2000	

*Returns:*

List of dictionairies containing the price and volume information for each requested tick.

```
[{'time': ..., 'close': ..., 'high': ..., 'low': ..., 'open': ...,
  'volumefrom': ..., 'volumeto': ...},
  {...},
 ...]
```

*Example 1:*

Get full price and volume data for the last five 5-minute segments.


```python
price_data = price.get_historical_data('BTC', 'USD', 'minute', aggregate=5, limit=5)
price_data
```




    [{'close': 4000.13,
      'high': 4005.94,
      'low': 3998.02,
      'open': 4003.43,
      'time': '2017-09-18 21:35:00',
      'volumefrom': 256.3,
      'volumeto': 1025563.77},
     {'close': 3996.59,
      'high': 4000.14,
      'low': 3990.96,
      'open': 4000.13,
      'time': '2017-09-18 21:40:00',
      'volumefrom': 229.67000000000002,
      'volumeto': 916935.5399999999},
     {'close': 4004.6,
      'high': 4004.92,
      'low': 3995.09,
      'open': 3996.59,
      'time': '2017-09-18 21:45:00',
      'volumefrom': 224.72,
      'volumeto': 898249.9400000001},
     {'close': 4011.07,
      'high': 4011.79,
      'low': 4003.43,
      'open': 4004.6,
      'time': '2017-09-18 21:50:00',
      'volumefrom': 267.78999999999996,
      'volumeto': 1071178.17},
     {'close': 4023.46,
      'high': 4025.98,
      'low': 4011.07,
      'open': 4011.07,
      'time': '2017-09-18 21:55:00',
      'volumefrom': 382.77,
      'volumeto': 1535682.04},
     {'close': 4012.24,
      'high': 4024.04,
      'low': 4010.38,
      'open': 4023.46,
      'time': '2017-09-18 22:00:00',
      'volumefrom': 377.92,
      'volumeto': 1507696.72}]



*Example 2:*

Get the ETH/USD trading volume in ETH for the last ten minutes.


```python
price_data = price.get_historical_data('ETH', 'USD', 'minute', info='volumefrom', aggregate=1, 
                                               limit=10)
price_data
```




    [{'time': '2017-09-18 21:53:00', 'volumefrom': 890.53},
     {'time': '2017-09-18 21:54:00', 'volumefrom': 255.69},
     {'time': '2017-09-18 21:55:00', 'volumefrom': 366.85},
     {'time': '2017-09-18 21:56:00', 'volumefrom': 139.25},
     {'time': '2017-09-18 21:57:00', 'volumefrom': 347.04},
     {'time': '2017-09-18 21:58:00', 'volumefrom': 552.24},
     {'time': '2017-09-18 21:59:00', 'volumefrom': 127.48},
     {'time': '2017-09-18 22:00:00', 'volumefrom': 1249.87},
     {'time': '2017-09-18 22:01:00', 'volumefrom': 370.06},
     {'time': '2017-09-18 22:02:00', 'volumefrom': 174.09},
     {'time': '2017-09-18 22:03:00', 'volumefrom': 0}]



*Example 3:*

Get the XRP closing prices in USD for the last ten days.


```python
price_data = price.get_historical_data('XRP', 'USD', 'day', info='close', aggregate=1, 
                                               limit=10)
price_data
```




    [{'close': 0.2122, 'time': '2017-09-08 02:00:00'},
     {'close': 0.213, 'time': '2017-09-09 02:00:00'},
     {'close': 0.2173, 'time': '2017-09-10 02:00:00'},
     {'close': 0.2143, 'time': '2017-09-11 02:00:00'},
     {'close': 0.2095, 'time': '2017-09-12 02:00:00'},
     {'close': 0.1983, 'time': '2017-09-13 02:00:00'},
     {'close': 0.1711, 'time': '2017-09-14 02:00:00'},
     {'close': 0.1846, 'time': '2017-09-15 02:00:00'},
     {'close': 0.1828, 'time': '2017-09-16 02:00:00'},
     {'close': 0.1814, 'time': '2017-09-17 02:00:00'},
     {'close': 0.191, 'time': '2017-09-18 02:00:00'}]



#### mining.py
* get_mining_equipment()

#### rest.py
* AllExchanges() (unfinished)

#### top.py
* get_top_exchanges_by_volume(fsym, tsym, limit=5)
* get_top_coins_by_volume(tsym, limit=20)
* get_top_pairs_by_volume(fsym, limit=5)
