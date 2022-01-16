from web3 import Web3
import json


class Binance_Config:
    """
    现货交易API网址：https://api.binance.com
    测试网API网址：	https://testnet.binance.vision
    """
    Apikey = ""
    secretKey = ""
    url = "https://api.binance.com"


class databases:
    host = 'localhost'
    user = 'user'
    port = 3306
    password = 'password'
    database = 'databse'

    DB_URI = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'


class OKex_Config:
    Apikey = ""
    secretKey = ""
    passphrase = ""


class bsc_config:
    bsc_rpc = "https://bsc-dataseed.binance.org/"
    # 工厂合约地址
    Factory_address = Web3.toChecksumAddress("0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73")
    # 工厂合约ABI文件
    Factory_ABI = json.loads('[{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":false,'
        '"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,'
        '"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address",'
        '"name":"token1","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},'
        '{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},'
        '{"constant":true,"inputs":[],"name":"INIT_CODE_PAIR_HASH","outputs":[{"internalType":"bytes32","name":"",'
        '"type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{'
        '"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address",'
        '"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,'
        '"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],'
        '"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{'
        '"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB",'
        '"type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],'
        '"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"feeTo",'
        '"outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view",'
        '"type":"function"},{"constant":true,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address",'
        '"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,'
        '"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"",'
        '"type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],'
        '"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{'
        '"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":false,'
        '"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address",'
        '"name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":false,'
        '"stateMutability":"nonpayable","type":"function"}]')
    # LP代币ABI文件
    LP_ABI = json.loads('[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},'
                        '{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner",'
                        '"type":"address"},{"indexed":true,"internalType":"address","name":"spender",'
                        '"type":"address"},{"indexed":false,"internalType":"uint256","name":"value",'
                        '"type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{'
                        '"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,'
                        '"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,'
                        '"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,'
                        '"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},'
                        '{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender",'
                        '"type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0",'
                        '"type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1",'
                        '"type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{'
                        '"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,'
                        '"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,'
                        '"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,'
                        '"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,'
                        '"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,'
                        '"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},'
                        '{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0",'
                        '"type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1",'
                        '"type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{'
                        '"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,'
                        '"internalType":"address","name":"to","type":"address"},{"indexed":false,'
                        '"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer",'
                        '"type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{'
                        '"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,'
                        '"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],'
                        '"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"",'
                        '"type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},'
                        '{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32",'
                        '"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},'
                        '{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},'
                        '{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{'
                        '"internalType":"uint256","name":"","type":"uint256"}],"payable":false,'
                        '"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{'
                        '"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256",'
                        '"name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool",'
                        '"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},'
                        '{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],'
                        '"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],'
                        '"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{'
                        '"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{'
                        '"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256",'
                        '"name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable",'
                        '"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{'
                        '"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view",'
                        '"type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{'
                        '"internalType":"address","name":"","type":"address"}],"payable":false,'
                        '"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],'
                        '"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0",'
                        '"type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},'
                        '{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,'
                        '"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{'
                        '"internalType":"address","name":"_token0","type":"address"},{"internalType":"address",'
                        '"name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,'
                        '"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],'
                        '"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],'
                        '"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{'
                        '"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{'
                        '"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,'
                        '"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],'
                        '"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],'
                        '"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{'
                        '"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{'
                        '"internalType":"uint256","name":"","type":"uint256"}],"payable":false,'
                        '"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{'
                        '"internalType":"address","name":"owner","type":"address"},{"internalType":"address",'
                        '"name":"spender","type":"address"},{"internalType":"uint256","name":"value",'
                        '"type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},'
                        '{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r",'
                        '"type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit",'
                        '"outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},'
                        '{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{'
                        '"internalType":"uint256","name":"","type":"uint256"}],"payable":false,'
                        '"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],'
                        '"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"",'
                        '"type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},'
                        '{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],'
                        '"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable",'
                        '"type":"function"},{"constant":false,"inputs":[{"internalType":"uint256",'
                        '"name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out",'
                        '"type":"uint256"},{"internalType":"address","name":"to","type":"address"},'
                        '{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],'
                        '"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,'
                        '"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],'
                        '"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],'
                        '"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable",'
                        '"type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{'
                        '"internalType":"address","name":"","type":"address"}],"payable":false,'
                        '"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1",'
                        '"outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,'
                        '"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],'
                        '"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],'
                        '"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{'
                        '"internalType":"address","name":"to","type":"address"},{"internalType":"uint256",'
                        '"name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool",'
                        '"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},'
                        '{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},'
                        '{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256",'
                        '"name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool",'
                        '"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
    # 区块链浏览器api key
    bscscan = ""

REDIS_HOST = "127.0.0.1"
REDIS_PORT = "6379"
REDIS_DB = "0"
REDIS_CONFIG = "redis://{}:{}/".format(REDIS_HOST, REDIS_PORT)
REDIS_URL = "{config}{db}".format(config=REDIS_CONFIG, db=REDIS_DB)

# telegram 频道ID
chat_id = 123456
bot_token = ""
shit_channel_id = 123456