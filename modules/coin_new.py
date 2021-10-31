from binance.spot import Spot as Client
from modules.HMAC import okex
from modules.coin_bot import send_message
from config import Binance_Config,databases
import requests
import json
import pymysql


spot_client = Client(Binance_Config.Apikey, Binance_Config.secretKey)


def mysql_add(table, coin):  # 添加数据到表
    db = pymysql.connect(host=databases.host,
                         user=databases.user,
                         password=databases.password,
                         database=databases.database)
    cursor = db.cursor()

    # SQL 插入语句
    sql = """INSERT INTO {}(coin)
             VALUES
             ('{}')""".format(table, coin)
    try:
        # 执行sql语句
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    # 关闭数据库连接
    db.close()


def differ(table, temp_table):  # 两张表比差
    db = pymysql.connect(host=databases.host,
                         user=databases.user,
                         password=databases.password,
                         database=databases.database)
    cursor = db.cursor()

    # SQL 插入语句
    sql = 'select distinct coin from {} where coin  not in (select coin  from {});'.format(temp_table, table)

    # 执行sql语句
    cursor.execute(sql)
    results = cursor.fetchall()
    ret = []
    for row in results:
        coin = row[0]
        ret.append(coin)
    db.close()
    return ret


def copy_table(table, temp_table):  # 复制两张表内容
    sql = """insert into {} select * from {};""".format(table, temp_table)
    db = pymysql.connect(host=databases.host,
                         user=databases.user,
                         password=databases.password,
                         database=databases.database)
    cursor = db.cursor()

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 向数据库提交
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()


def truncate(table):  # 清空数据表
    db = pymysql.connect(host=databases.host,
                         user=databases.user,
                         password=databases.password,
                         database=databases.database)
    cursor = db.cursor()
    sql = """truncate table {}""".format(table)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 向数据库提交
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()


def binance_differ():
    truncate("binance_temp_coin")  # 清空临时数据表
    data = spot_client.coin_info()  # 获取币安钱包数据
    for i in data:
        mysql_add("binance_temp_coin", i["coin"])  # 写入临时数据表

    data = differ("binance_coin", "binance_temp_coin")  # 获取比差数据
    if data:
        truncate("binance_coin")  # 清空基础数据表
        copy_table("binance_coin", "binance_temp_coin")  # 更新基础数据表至最新数据
        for i in data:
            send_message("币安交易所钱包增加了新的币种 #{}，请注意币安公告".format(i))  # 推送本次上币信息
    else:
        pass


def huobi_differ():
    url = "https://api.huobi.pro/v1/common/currencys"
    coin = json.loads(requests.get(url=url).text)  # 获取火币所有币种数据
    truncate("huobi_temp_coin")  # 清空临时数据表

    if coin["status"] == "ok":
        for i in coin["data"]:
            mysql_add("huobi_temp_coin", i)

        data = differ("huobi_coin", "huobi_temp_coin")  # 获取比差数据
        if data:
            truncate("huobi_coin")  # 清空基础数据表
            copy_table("huobi_coin", "huobi_temp_coin")  # 更新基础数据表至最新数据
            for i in data:
                send_message("火币交易所钱包增加了新的币种 #{}，请注意火币公告".format(i.upper()))  # 推送本次上币信息
        else:
            pass

    else:
        send_message("火币[获取所有币种]接口故障，请检查")


def okex_differ():
    host = "https://www.okex.com"
    requestPath = "/api/v5/asset/currencies"
    headers = okex(method="GET", requestPath=requestPath, body="").gen_sign()
    coin = json.loads(requests.get(url=host + requestPath, headers=headers).text)  # 获取OKEX所有币种数据
    truncate("okex_temp_coin")  # 清空临时数据表
    if coin["code"] == "0":
        temp_coin = []
        for i in coin["data"]:
            temp_coin.append(i["ccy"])
        for coin in list(set(temp_coin)):  # 去重
            mysql_add("okex_temp_coin", coin)
        data = differ("okex_coin", "okex_temp_coin")  # 获取比差数据
        if data:
            truncate("okex_coin")  # 清空基础数据表
            copy_table("okex_coin", "okex_temp_coin")  # 更新基础数据表至最新数据
            for i in data:
                send_message("OKEX交易所钱包增加了新的币种 #{}，请注意OKEX公告".format(i.upper()))  # 推送本次上币信息
        else:
            pass
    else:
        send_message("OKEX[获取币种列表]接口故障，请检查")


def mexc_differ():
    # url = "https://www.mexc.com/open/api/v2/market/symbols"
    url = "https://www.mexc.com/open/api/v2/market/coin/list"
    coin = json.loads(requests.get(url=url).text)
    truncate("mexc_temp_coin")
    if coin["code"] == 200:
        temp_coin = []
        for i in coin["data"]:
            temp_coin.append(i['currency'])
        for coin in list(set(temp_coin)):
            mysql_add("mexc_temp_coin", coin)
        data = differ("mexc_coin", "mexc_temp_coin")  # 获取比差数据
        if data:
            truncate("mexc_coin")  # 清空基础数据表
            copy_table("mexc_coin", "mexc_temp_coin")  # 更新基础数据表至最新数据
            for i in data:
                send_message("MEXC交易所钱包增加了新的币种 #{}，请注意MEXC公告".format(i.upper()))  # 推送本次上币信息
        else:
            pass
    else:
        send_message("MEXC[所有交易对信息]接口故障，请检查")


def gateio_differ():
    url = "https://api.gateio.ws/api/v4/spot/currency_pairs"  # gate.io v4 api
    try:
        coin = json.loads(requests.get(url=url).text)
        truncate("gateio_temp_coin")
        temp_coin = []
        for i in coin:
            temp_coin.append(i['base'])
        for c in list(set(temp_coin)):
            mysql_add("gateio_temp_coin", c)
        data = differ("gateio_coin", "gateio_temp_coin")  # 获取比差数据
        if data:
            truncate("gateio_coin")  # 清空基础数据表
            copy_table("gateio_coin", "gateio_temp_coin")  # 更新基础数据表至最新数据
            for i in data:
                send_message("Gate.io交易所钱包增加了新的币种 #{}，请注意Gate.io公告".format(i.upper()))  # 推送本次上币信息
        else:
            pass
    except:
        send_message("Gate.io[查询支持的所有交易对]接口故障，请检查")


def coinbase_differ():
    url = "https://api.exchange.coinbase.com/currencies"
    coin = json.loads(requests.get(url=url).text)
    truncate("coinbase_temp_coin")
    try:
        temp_coin = []
        for i in coin:
            temp_coin.append(i['id'])
        for coin in list(set(temp_coin)):
            mysql_add("coinbase_temp_coin", coin)
        data = differ("coinbase_coin", "coinbase_temp_coin")  # 获取比差数据
        if data:
            truncate("coinbase_coin")  # 清空基础数据表
            copy_table("coinbase_coin", "coinbase_temp_coin")  # 更新基础数据表至最新数据
            for i in data:
                send_message("coinbase交易所钱包增加了新的币种 #{}，请注意coinbase公告".format(i.upper()))  # 推送本次上币信息
        else:
            pass
    except:
        send_message("coinbase[Get all known currencies]接口故障，请检查")


def kucoin_differ():
    url = "https://api.kucoin.com/api/v1/symbols"
    coin = json.loads(requests.get(url=url).text)
    truncate("coinbase_temp_coin")
    if coin['code'] == "200000":
        temp_coin = []
        for i in coin["data"]:
            temp_coin.append(i['baseCurrency'])
        for coin in list(set(temp_coin)):
            mysql_add("kucoin_temp_coin", coin)
        data = differ("kucoin_coin", "kucoin_temp_coin")  # 获取比差数据
        if data:
            truncate("kucoin_coin")  # 清空基础数据表
            copy_table("kucoin_coin", "kucoin_temp_coin")  # 更新基础数据表至最新数据
            for i in data:
                send_message("kucoin交易所钱包增加了新的币种 #{}，请注意kucoin公告".format(i.upper()))  # 推送本次上币信息
        else:
            pass
    else:
        send_message("kucoin[所有交易对信息]接口故障，请检查")


def ftx_differ():
    url = "https://ftx.com/api/wallet/coins"
    coin = json.loads(requests.get(url=url).text)
    truncate("ftx_temp_coin")
    if coin['success']:
        temp_coin = []
        for i in coin["result"]:
            if i["canDeposit"] and i["canWithdraw"] and i["canConvert"] == True:
                temp_coin.append(i['id'])
        for coin in list(set(temp_coin)):
            mysql_add("ftx_temp_coin", coin)
        data = differ("ftx_coin", "ftx_temp_coin")  # 获取比差数据
        if data:
            truncate("ftx_coin")  # 清空基础数据表
            copy_table("ftx_coin", "ftx_temp_coin")  # 更新基础数据表至最新数据
            for i in data:
                send_message("FTX交易所钱包增加了新的币种 #{}，请注意FTX公告".format(i.upper()))  # 推送本次上币信息
        else:
            pass
    else:
        send_message("FTX[所有交易对信息]接口故障，请检查")