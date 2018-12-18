# -*- coding: utf-8 -*-
import time
from configs.config import logger


def alarm(h,m=0,s=0):
    """当前时间大于预设时间就进行下面函数执行，否则sleep 1秒"""
    status = True
    while True:
        # 拼接设置的时间为时间戳
        str_time = time.strftime("%Y-%m-%d", time.localtime()) + f" {h}:{m}:{s}"
        # 将字符串时间戳改为时间戳数字
        timeStamp = int(time.mktime(time.strptime(str_time, "%Y-%m-%d %H:%M:%S")))
        now_time = time.time()
        if status:
            logger.info(f"set clock at :{str_time}---{timeStamp}")
            logger.info(f'now time is :{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}---{now_time}')
            status = False
        if now_time >= timeStamp:
            logger.info("开始执行下面函数")
            return True
        time.sleep(3)
        logger.info("dadada~")

# alarm(14,28,0)