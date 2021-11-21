from binance.spot import Spot as Client
from modules.HMAC import okex
from modules.coin_bot import send_message
from config import Binance_Config
from modules.sql.coin_db import *
import requests
import json

spot_client = Client(Binance_Config.Apikey, Binance_Config.secretKey)


def binance_build():
    ret_data = spot_client.coin_info()  # 获取币安钱包数据
    for i in ret_data:
        binance.add(i)


def huobi_build():
    url = "https://api.huobi.pro/v1/common/currencys"
    coin = json.loads(requests.get(url=url).text)  # 获取火币所有币种数据
    if coin["status"] == "ok":
        for i in coin["data"]:
            huobi.add(i)


    else:
        send_message("火币[获取所有币种]接口故障，请检查")


def okex_build():
    host = "https://www.okex.com"
    requestPath = "/api/v5/asset/currencies"
    headers = okex(method="GET", requestPath=requestPath, body="").gen_sign()
    coin = json.loads(requests.get(url=host + requestPath, headers=headers).text)  # 获取OKEX所有币种数据
    if coin["code"] == "0":
        temp_coin = []
        for i in coin["data"]:
            temp_coin.append(i["ccy"])
        for coin in list(set(temp_coin)):  # 去重
            okex.add(coin)


    else:
        send_message("OKEX[获取币种列表]接口故障，请检查")


def mexc_build():
    url = "https://www.mexc.com/open/api/v2/market/coin/list"
    coin = json.loads(requests.get(url=url).text)
    if coin["code"] == 200:
        temp_coin = []
        for i in coin["data"]:
            temp_coin.append(i['currency'])
        for coin in list(set(temp_coin)):
            okex.add(coin)
    else:
        send_message("MEXC[所有交易对信息]接口故障，请检查")


def gateio_build():
    url = "https://api.gateio.ws/api/v4/spot/currency_pairs"  # gate.io v4 api
    try:
        coin = json.loads(requests.get(url=url).text)
        temp_coin = []
        for i in coin:
            temp_coin.append(i['base'])
        for c in list(set(temp_coin)):
            gateio.add(c)
    except:
        send_message("Gate.io[查询支持的所有交易对]接口故障，请检查")


def coinbase_build():
    url = "https://api.exchange.coinbase.com/currencies"
    coin = json.loads(requests.get(url=url).text)
    try:
        temp_coin = []
        for i in coin:
            temp_coin.append(i['id'])
        for coin in list(set(temp_coin)):
            coinbase.add(coin)
    except:
        send_message("coinbase[Get all known currencies]接口故障，请检查")


def kucoin_build():
    url = "https://api.kucoin.com/api/v1/symbols"
    coin = json.loads(requests.get(url=url).text)
    if coin['code'] == "200000":
        temp_coin = []
        for i in coin["data"]:
            temp_coin.append(i['baseCurrency'])
        for coin in list(set(temp_coin)):
            kucoin.add(coin)
    else:
        send_message("kucoin[所有交易对信息]接口故障，请检查")


def ftx_build():
    url = "https://ftx.com/api/wallet/coins"
    coin = json.loads(requests.get(url=url).text)
    if coin['success']:
        temp_coin = []
        for i in coin["result"]:
            if i["canDeposit"] and i["canWithdraw"] and i["canConvert"] == True:
                temp_coin.append(i['id'])
        for coin in list(set(temp_coin)):
            ftx.add(coin)
    else:
        send_message("FTX[所有交易对信息]接口故障，请检查")
