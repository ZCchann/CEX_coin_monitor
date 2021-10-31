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


# telegram 频道ID
chat_id = 123456
bot_token = ""
