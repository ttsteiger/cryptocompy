from tests.cryptocompy_vcr import cryptocompy_vcr

from cryptocompy import top


@cryptocompy_vcr.use_cassette()
def test_get_top_exchanges():
    top_exchanges = top.get_top_exchanges('BTC', 'USD')

    assert len(top_exchanges) == 5
    coinbase_exchange = top_exchanges[1]

    coinbase_exchange['exchange'] == 'Coinbase'
    coinbase_exchange['fromSymbol'] == 'BTC'
    coinbase_exchange['toSymbol'] == 'USD'
    coinbase_exchange['volume24h'] == 3076.1831993199976
    coinbase_exchange['volume24hTo'] == 20191108.061967414


@cryptocompy_vcr.use_cassette()
def test_get_top_coins():

    topcoin = top.get_top_coins('USD')
    assert len(topcoin) == 21
    btc = topcoin[1]

    assert btc['SYMBOL'] == 'BTC'
    assert btc['SUPPLY'] == 17296550
    assert btc['FULLNAME'] == 'Bitcoin (BTC)'
    assert btc['NAME'] == 'Bitcoin'
    assert btc['ID'] == '1182'
    assert btc['VOLUME24HOURTO'] == 178522647.1706209


@cryptocompy_vcr.use_cassette()
def test_get_top_pairs():

    toppairs = top.get_top_pairs('BTC')
    assert len(toppairs) == 5
    usd_pair = toppairs[1]

    assert usd_pair['exchange'] == 'CCCAGG'
    assert usd_pair['fromSymbol'] == 'BTC'
    assert usd_pair['toSymbol'] == 'USD'
    assert usd_pair['volume24h'] == 27103.1083762061
    assert usd_pair['volume24hTo'] == 178887913.40238342
