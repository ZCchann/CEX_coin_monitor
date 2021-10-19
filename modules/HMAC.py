import datetime
import hmac
import base64
import config


class okex:
    def __init__(self, method, requestPath, body):
        self.method = method
        self.requestPath = requestPath
        self.body = body
        self.Apikey = config.OKex_Config.Apikey
        self.secretKey = config.OKex_Config.secretKey
        self.passphrase = config.OKex_Config.passphrase

    @staticmethod
    def get_timestamp():
        now = datetime.datetime.utcnow()
        t = now.isoformat("T", "milliseconds")
        return t + "Z"

    @staticmethod
    def sign(message, secretKey):
        mac = hmac.new(secretKey.encode("utf-8"), message.encode("utf-8"), digestmod='sha256')
        d = mac.digest()
        return base64.b64encode(d)

    def gen_sign(self):
        timestamp = okex.get_timestamp()
        s = str(timestamp) + str.upper(self.method) + str(self.requestPath) + str(self.body)

        return {
            "OK-ACCESS-KEY": self.Apikey,
            "OK-ACCESS-SIGN": str(okex.sign(s, self.secretKey)),
            "OK-ACCESS-TIMESTAMP": str(timestamp),
            "OK-ACCESS-PASSPHRASE": self.passphrase,
            "Content-Type": "application/json"
        }
