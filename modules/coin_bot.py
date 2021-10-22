import config
import requests
import json


def send_message(message):
    url = "https://api.telegram.org/bot{}/sendMessage".format(config.bot_token)
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "chat_id": config.chat_id,  # 对话id。若是频道则为“@channel_id”
        "text": str(message),  # 发送的信息正文。可以使用有限的几种 Markdown/HTML 进行标记
        "parse_mode": "MarkdownV2"  # 使用markdown解析传送消息
    }

    requests.post(url=url, data=json.dumps(data), headers=headers)
