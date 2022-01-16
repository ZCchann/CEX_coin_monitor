from web3.logs import DISCARD
from modules.shit_coin import web3, coin_redis
from config import bsc_config
from decimal import Decimal
import json
import time


def swap_log(transactionHash):
    """
    定义几个常见的币对
    """
    busd = "0x55d398326f99059fF775485246999027B3197955"
    wbnb = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
    usdt_bep20 = "0x55d398326f99059fF775485246999027B3197955"
    log = web3.eth.get_transaction_receipt(transactionHash)  # 获取交易事件的详细日志
    logs_contract = web3.eth.contract(address=bsc_config.Factory_address, abi=bsc_config.Factory_ABI)
    PairCreated_log = json.loads(web3.toJSON(logs_contract.events.PairCreated().processReceipt(log, errors=DISCARD)))[
        0]  # 获取工厂合约代币添加事件
    """
    判断交易对是否为BNB/BUSD
    """
    ret_data = {
        "pancake_LP_token": PairCreated_log["args"]["pair"],
    }
    if PairCreated_log["args"]["token0"] == busd:
        ret_data.update({"coin": "BUSD"})
    elif PairCreated_log["args"]["token0"] == wbnb:
        ret_data.update({"coin": "BNB"})
    elif PairCreated_log["args"]["token0"] == usdt_bep20:
        ret_data.update({"coin": "USDT-BEP20"})
    else:
        ret_data.update({"contract": PairCreated_log["args"]["token0"]})

    if PairCreated_log["args"]["token1"] == busd:
        ret_data.update({"coin": "BUSD"})
    elif PairCreated_log["args"]["token1"] == wbnb:
        ret_data.update({"coin": "BNB"})
    elif PairCreated_log["args"]["token1"] == usdt_bep20:
        ret_data.update({"coin": "USDT-BEP20"})
    else:
        ret_data.update({"contract": PairCreated_log["args"]["token1"]})

    return ret_data


def decode_abi(contract_address):
    data_abi = [
        {'inputs': [], 'name': 'symbol', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}],
         'stateMutability': 'view', 'type': 'function'},
        {'inputs': [], 'name': 'totalSupply', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
         'stateMutability': 'view', 'type': 'function'},
        {'inputs': [], 'name': 'name', 'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}],
         'stateMutability': 'view', 'type': 'function'}]
    # 此ABI只解析以下内容：1.name 代币名称(例:ether) 2.symbol 代币符号(例：ETH) 3.totalSupply 发行总量
    decode_contract = web3.eth.contract(address=contract_address, abi=data_abi)

    ret_data = {
        "symbol": decode_contract.functions.symbol().call(),
        "name": decode_contract.functions.name().call(),
        "totalSupply": web3.fromWei(decode_contract.functions.totalSupply().call(), 'ether')
    }
    return ret_data


def Factory_listen():
    block_filter = web3.eth.filter({'toBlock': "pending", 'address': bsc_config.Factory_address})
    while True:
        try:
            for event in block_filter.get_new_entries():
                transactionHash = event.transactionHash.hex()  # 返回交易哈希
                try:
                    ret_data = swap_log(transactionHash)
                    abi_data = decode_abi(ret_data["contract"])
                    token_address = ret_data["contract"]  # 合约地址
                    coin_name = abi_data["name"]  # 代币名称
                    symbol = abi_data["symbol"]  # 代币符号
                    totalSupply = int(Decimal(abi_data["totalSupply"]))  # 代币发行总量 单位：ether
                    to_coin = ret_data["coin"]  # 交易对 与谁交易
                    LP_token_address = ret_data["pancake_LP_token"]  # LP合约地址
                    if totalSupply > 1000000:  # 发币数量大于100万
                        coin_redis.hmset(name=token_address, mapping={
                            "token_address": token_address,
                            "coin_name": coin_name,
                            "symbol": symbol,
                            "totalSupply": totalSupply,
                            "to_coin": to_coin,
                            "LP_token_address": LP_token_address
                        })
                except:
                    pass
        except ValueError:
            time.sleep(2)
