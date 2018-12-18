# -*- coding: utf-8 -*-

from core_spider.jd_goods_details import JD_Spider
from core_spider.jd_list import List_spider
from tools.mongo_tools import Mongo_db
from tools.clock import alarm
from datas.analys import get_deep_price_down
from configs.config import logger

import time

def run():

    # 先运行搜索 获取到商品的id 插入mongo
    # l = List_spider("华为手机", 10)
    # l.run()

    # 从mongo拿到id 查询商品的详细信息
    m = Mongo_db()
    # 查询所有的，限制1000条
    res = m.search({}, 2, 1000)
    count = 0
    for i in res:
        count += 1
        sku_id = i.get("sku_id", "")
        if not sku_id:
            continue
        jd = JD_Spider(sku_id)
        jd.run()
    print(count)



while True:
    # 设置运行闹钟 每天晚上9点开始运行
    alarm(17, 39, 0)
    logger.info(f"it‘s time to run~now is {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
    # 运行数据更新
    logger.info(f'start run ~')
    # run()
    # time.sleep(10*60)
    # 等一个小时后运行数据分析
    get_deep_price_down()
    # 程序睡到第二天后继续
    time.sleep(60*60*10)