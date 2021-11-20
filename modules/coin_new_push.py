from binance.spot import Spot as Client
from modules.HMAC import okex
from modules.coin_bot import send_message
from config import Binance_Config
from modules.sql.coin_db import *
import requests
import json
import time

spot_client = Client(Binance_Config.Apikey, Binance_Config.secretKey)


def binance_differ():
    ret_data = spot_client.coin_info()  # 获取币安钱包数据
    data = []
    for i in ret_data:
        data.append(i["coin"])  # 写入临时数据表

    dif = list(set(data).difference(set(binance.query())))  # 比差集
    if dif:
        for i in dif:
            binance.add(i)
            send_message("币安交易所钱包增加了新的币种 #{}，请注意币安公告".format(i))  # 推送本次上币信息
            time.sleep(1)
    else:
        pass


def huobi_differ():
    url = "https://api.huobi.pro/v1/common/currencys"
    coin = json.loads(requests.get(url=url).text)  # 获取火币所有币种数据
    data = []
    if coin["status"] == "ok":
        for i in coin["data"]:
            data.append(i)

        # data = differ("huobi_coin", "huobi_temp_coin")  # 获取比差数据

        dif = list(set(data).difference(set(huobi.query())))  # 比差集
        if dif:
            for i in dif:
                huobi.add(i)
                send_message("火币交易所钱包增加了新的币种 #{}，请注意火币公告".format(i.upper()))  # 推送本次上币信息
                time.sleep(1)
        else:
            pass

    else:
        send_message("火币[获取所有币种]接口故障，请检查")


def okex_differ():
    host = "https://www.okex.com"
    requestPath = "/api/v5/asset/currencies"
    headers = okex(method="GET", requestPath=requestPath, body="").gen_sign()
    coin = json.loads(requests.get(url=host + requestPath, headers=headers).text)  # 获取OKEX所有币种数据
    # truncate("okex_temp_coin")  # 清空临时数据表
    data = []
    if coin["code"] == "0":
        temp_coin = []
        for i in coin["data"]:
            temp_coin.append(i["ccy"])
        for coin in list(set(temp_coin)):  # 去重
            data.append(coin)

        dif = list(set(data).difference(set(okex.query())))  # 比差集
        if dif:
            for i in dif:
                okex.add(i)
                send_message("OKEX交易所钱包增加了新的币种 #{}，请注意OKEX公告".format(i.upper()))  # 推送本次上币信息
                time.sleep(1)
        else:
            pass
    else:
        send_message("OKEX[获取币种列表]接口故障，请检查")


def mexc_differ():
    url = "https://www.mexc.com/open/api/v2/market/coin/list"
    coin = json.loads(requests.get(url=url).text)
    data = []
    if coin["code"] == 200:
        temp_coin = []
        for i in coin["data"]:
            temp_coin.append(i['currency'])
        for coin in list(set(temp_coin)):
            data.append(coin)
        dif = list(set(data).difference(set(mexc.query())))  # 比差集
        if dif:
            for i in dif:
                mexc.add(i)
                send_message("MEXC交易所钱包增加了新的币种 #{}，请注意MEXC公告".format(i.upper()))  # 推送本次上币信息
                time.sleep(1)
        else:
            pass
    else:
        send_message("MEXC[所有交易对信息]接口故障，请检查")


def gateio_differ():
    url = "https://api.gateio.ws/api/v4/spot/currency_pairs"  # gate.io v4 api
    try:
        coin = json.loads(requests.get(url=url).text)
        data = []
        temp_coin = []
        for i in coin:
            temp_coin.append(i['base'])
        for c in list(set(temp_coin)):
            data.append(c)
        dif = list(set(data).difference(set(gateio.query())))  # 比差集
        if dif:
            for i in dif:
                gateio.add(i)
                send_message("Gate.io交易所钱包增加了新的币种 #{}，请注意Gate.io公告".format(i.upper()))  # 推送本次上币信息
                time.sleep(1)
        else:
            pass
    except:
        send_message("Gate.io[查询支持的所有交易对]接口故障，请检查")


def coinbase_differ():
    url = "https://api.exchange.coinbase.com/currencies"
    coin = json.loads(requests.get(url=url).text)
    try:
        data = []
        temp_coin = []
        for i in coin:
            temp_coin.append(i['id'])
        for coin in list(set(temp_coin)):
            data.append(coin)
        dif = list(set(data).difference(set(coinbase.query())))  # 比差集
        if dif:
            for i in dif:
                coinbase.add(i)
                send_message("coinbase交易所钱包增加了新的币种 #{}，请注意coinbase公告".format(i.upper()))  # 推送本次上币信息
        else:
            pass
    except:
        send_message("coinbase[Get all known currencies]接口故障，请检查")


def kucoin_differ():
    url = "https://api.kucoin.com/api/v1/symbols"
    coin = json.loads(requests.get(url=url).text)
    if coin['code'] == "200000":
        temp_coin = []
        data = []
        for i in coin["data"]:
            temp_coin.append(i['baseCurrency'])
        for coin in list(set(temp_coin)):
            data.append(coin)
        dif = list(set(data).difference(set(kucoin.query())))  # 比差集
        if dif:
            for i in dif:
                kucoin.add(i)
                send_message("kucoin交易所钱包增加了新的币种 #{}，请注意kucoin公告".format(i.upper()))  # 推送本次上币信息
        else:
            pass
    else:
        send_message("kucoin[所有交易对信息]接口故障，请检查")


def ftx_differ():
    url = "https://ftx.com/api/wallet/coins"
    coin = json.loads(requests.get(url=url).text)
    if coin['success']:
        temp_coin = []
        data = []
        for i in coin["result"]:
            if i["canDeposit"] and i["canWithdraw"] and i["canConvert"] == True:
                temp_coin.append(i['id'])
        for coin in list(set(temp_coin)):
            data.append(coin)
        dif = list(set(data).difference(set(ftx.query())))  # 比差集
        if dif:
            for i in dif:
                ftx.add(i)
                send_message("FTX交易所钱包增加了新的币种 #{}，请注意FTX公告".format(i.upper()))  # 推送本次上币信息
        else:
            pass
    else:
        send_message("FTX[所有交易对信息]接口故障，请检查")
