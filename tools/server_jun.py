# -*- coding: utf-8 -*-

import requests
from configs.config import logger


SERVER_JUN_URL = "http://sc.ftqq.com/SCU37154T6493d663e2f8d5bccb44ee60986abb0c5c08f47d89024.send"
def send_2_me(text, desp):
    r = requests.post(SERVER_JUN_URL, data={'text': text, 'desp': desp})
    logger.info(r.status_code)
    logger.info("tell me success!")