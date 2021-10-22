#!/usr/bin/env python3
from modules.coin_new import *
from modules.scraping import binance
import threading

if __name__ == '__main__':
    threadpool = [threading.Thread(target=binance_differ()),
                  threading.Thread(target=huobi_differ()),
                  threading.Thread(target=okex_differ()),
                  threading.Thread(target=mexc_differ()),
                  threading.Thread(target=gateio_differ()),
                  threading.Thread(target=coinbase_differ()),
                  threading.Thread(target=kucoin_differ()),
                  threading.Thread(target=ftx_differ()),
                  threading.Thread(target=binance())
                  ]
    for th in threadpool:
        th.start()
    for th in threadpool:
        th.join()
