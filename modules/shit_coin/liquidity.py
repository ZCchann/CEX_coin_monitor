from modules.shit_coin import web3, coin_redis
from config import bsc_config
from modules.shit_coin.abi_check import abi_check
from modules.coin_bot import send_message
import config


def reserve_LPtoken(contrace_address):
    WBNB = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
    contract = web3.eth.contract(address=web3.toChecksumAddress(contrace_address),
                                 abi=bsc_config.LP_ABI)
    token0 = contract.functions.token0().call()
    token1 = contract.functions.token1().call()
    ret = contract.functions.getReserves().call()
    if ret[0] == 0 and ret[1] == 0:
        return 0
    else:
        if token0 == WBNB:
            reserve = ret[0]
            return web3.fromWei(reserve, 'ether')
        if token1 == WBNB:
            reserve = ret[1]
            return web3.fromWei(reserve, 'ether')


def LiquidityETH():
    for i in coin_redis.keys():
        LPtoken = coin_redis.hget(i, "LP_token_address")
        reserve = reserve_LPtoken(LPtoken)
        if reserve != 0:
            if reserve >= 5:
                coin = coin_redis.hgetall(name=i)
                contract_check = abi_check(i)
                message = "pancake添加了新的交易币对:\n代币名称:{}\n代币符号:{}\n代币总发行量:{}\n交易对:{}\n当前流动性池BNB数量:{}\n合约源码情况:{}\n合约地址:{}\npancake LP代币地址:{}".format(
                    coin["coin_name"], coin["symbol"], coin["totalSupply"], coin["to_coin"], reserve,
                    (contract_check, coin["burn"]),
                    coin["token_address"], coin["LP_token_address"])
                coin_redis.delete(i)
                send_message(message, config.shit_channel_id)
