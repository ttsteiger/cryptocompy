from tests.cryptocompy_vcr import cryptocompy_vcr

from cryptocompy import mining


@cryptocompy_vcr.use_cassette()
def test_get_mining_contracts():
    coin_data, mining_contracts = mining.get_mining_contracts()

    assert coin_data == {}
    assert len(mining_contracts) == 192

    assert '16762' in mining_contracts.keys()
    eth_mining_contract = mining_contracts['16762']

    assert eth_mining_contract["Name"] == 'Ethereum Large Mining Contract'
    assert eth_mining_contract["Currency"] == 'USD'
    assert eth_mining_contract["CurrenciesAvailable"] == 'ETH'
    assert eth_mining_contract["Algorithm"] == 'Ethash'


@cryptocompy_vcr.use_cassette()
def test_get_mining_equipment():

    mining_equipments = mining.get_mining_equipment()

    assert len(mining_equipments) == 139

    assert '10980' in mining_equipments.keys()
    bitmain = mining_equipments['10980']

    assert bitmain['Company'] == 'BitMain'
    assert bitmain['Name'] == 'AntMiner S7 Batch 10'
    assert bitmain['Currency'] == 'USD'
    assert bitmain['EquipmentType'] == 'ASIC'
    assert bitmain['CurrenciesAvailable'] == 'BTC'
