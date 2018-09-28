import pytest
from tests.cryptocompy_vcr import cryptocompy_vcr

from cryptocompy import coin as cryptocompy_coin


@cryptocompy_vcr.use_cassette()
def test_get_coin_list():
    coins = cryptocompy_coin.get_coin_list(coins='all')
    assert len(coins) == 3098

    assert 'BTC' in coins.keys()
    assert 'ETH' in coins.keys()

    btc = coins['BTC']
    assert btc
    assert btc['Id'] == '1182'
    assert btc['Name'] == 'BTC'
    assert btc['Symbol'] == 'BTC'
    assert btc['CoinName'] == 'Bitcoin'


@cryptocompy_vcr.use_cassette()
@pytest.mark.parametrize("coins_asked, coins_recieved", [
    ([], []),
    ("BTC", ["BTC"]),
    (["BTC"], ["BTC"]),
    (["BTC", "ETH"], ["BTC", "ETH"]),
])
def test_get_specific_coins(coins_asked, coins_recieved):
    coins = cryptocompy_coin.get_coin_list(coins=coins_asked)

    assert set(coins.keys()) == set(coins_recieved)


def test_get_invalid_coin():
    pass


@cryptocompy_vcr.use_cassette()
@pytest.mark.parametrize("coin, fiat, number_exchanges, price", [
    ('BTC', 'USD', 66, 6531.6),
    ('BTC', 'EUR', 45, 5638.8),
    ('ETH', 'USD', 48, 229.0),
    ('ETH', 'EUR', 25, 197.88),
])
def test_get_coin_snapshot(coin, fiat, number_exchanges, price):
    res = cryptocompy_coin.get_coin_snapshot(coin, fiat)
    assert res

    exchanges = res['Exchanges']
    assert len(exchanges) == number_exchanges

    kraken_exchanges = [ex for ex in exchanges if ex['MARKET'] == 'Kraken']
    assert kraken_exchanges
    kraken_exchange = kraken_exchanges[0]

    assert kraken_exchange['MARKET'] == 'Kraken'
    assert kraken_exchange['FROMSYMBOL'] == coin
    assert kraken_exchange['TOSYMBOL'] == fiat
    assert float(kraken_exchange['PRICE']) == price


def test_get_invalid_coin_snapshot():
    pass
