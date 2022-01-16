import requests
import config
import json


def abi_check(contract_address):
    url = "https://api.bscscan.com/api?module=contract&action=getabi&address={}&apikey={}".format(contract_address,
                                                                                                  config.bsc_config.bscscan)
    ret = json.loads(requests.get(url=url).text)
    if ret["status"] == "0" and ret["result"] == "Contract source code not verified":
        return "合约未开源"
    elif ret["status"] == "1":
        return "合约已开源"
