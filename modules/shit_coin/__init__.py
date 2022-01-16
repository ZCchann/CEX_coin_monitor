from web3 import Web3
import config
import redis

web3 = Web3(Web3.HTTPProvider(config.bsc_config.bsc_rpc))  # 初始化web3

coin_redis = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, decode_responses=True, db=config.REDIS_DB)