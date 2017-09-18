
# cryptocomparepython
Simple wrapper for the public CryptoCompare API.

Cryptocompare API:
https://www.cryptocompare.com/api


## ToDo:

- add all get functions
- complete docstrings
- create readme with examples
- error handling for http requests
- throw warnings for conversions

## Installation

dsfsdfdsfsdfds
sdfsdfdfsdfsdfsdf
sdfsdfdsfsdfsdfsdf
sfsdfsdfdsfffsdfsdf
fdsdfsdfsdfds

## Contributing

If you would like to help me with my work or have any suggestions for improvements please follow the "fork-and-pull" Git workflow.

1. Fork the repo on GitHub
2. Clone the project to your own machine
3. Commit changes to your own branch
4. Push your work back up to your fork
5. Submit a Pull request so that we can review your changes

NOTE: Be sure to merge the latest from "upstream" before making a pull request!


## Functions

### coin.py

#### get_coin_list(coins='all')

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




    ['TAGR', 'MTX', 'LC', 'CHA', 'TRUMP', 'KORE', 'MYB', 'ELC', 'KGC', 'EQM']



#### get_coin_snapshot(fsym, tsym)

Get blockchain information, aggregated data as well as data for the individual exchanges available for the specified currency pair.

*Arguments:*

`fsym`: FROM symbol.
`tsym`: TO symbol. Blockchain information will only be returned if this parameter is a fiat currency.

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




    659973.6200995498



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


```python

```


```python

```


```python

```
