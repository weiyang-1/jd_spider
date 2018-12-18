# -*- coding: utf-8 -*-

from tools.mongo_tools import Mongo_db
import time
from configs.config import logger
from tools.server_jun import send_2_me


m = Mongo_db()

def get_deep_price_down():
    """获取商品的信息"""
    Min_pre = 0  # 定义降价比例对象
    Min_info = None  # 定义最低折扣商品信息
    Max_price_down = 0  # 定义最大降价值
    Max_price_info = None  # 定义降价最多商品信息
    Text_min_pre = "降价百分比最多商品"
    Text_min_price = "降价数值最多商品"


    with open("../datas/result.csv", mode="w", encoding="utf-8", errors="ignore") as f:
        res = m.search({},type=2, count=1000)
        for i in res:
            time.sleep(0.001)
            sku_id = i.get("sku_id", "")
            name = i.get("name", "")
            p1 = i.get("p1", 0)
            url = f'https://item.jd.com/{sku_id}.html'
            if not p1:
                continue
            p13 = i.get(f'p1-{time.strftime("%Y-%m-%d", time.localtime())}', 0)
            if not p13:
                continue
            # print(f"this p1:{p1}---p3:{p13}")
            if float(p1) < 100:
                continue
            # p12 = i.get("p1-2018-12-15", 0)
            if float(p13) < 100:
                continue
            price_down = float(p1) - float(p13)
            pre_count = price_down / float(p1) * 100
            if not price_down:
                logger.info("价格没变")
            else:
                logger.info("价格改变")
                res = sku_id + "," + name + "," + str(p1) + "," + str(p13) + "," + str(price_down) + "," + str(pre_count)+ "," + url + "\n"
                f.write(res)
                logger.info(res)

            res_phone = "####" + name + "---" + str(p1) + "---" + str(p13) + "---" + str(price_down) + "---" + str(pre_count)+ "---" + url + "\n"
            if Min_pre <= pre_count:
                Min_pre = pre_count  # 获取到最小的折扣信息商品
                Min_info = res_phone

            if Max_price_down <= price_down:
                Max_price_down = price_down
                Max_price_info = res_phone


        # tell_me
        send_2_me(Text_min_pre, Min_info)
        time.sleep(60)
        send_2_me(Text_min_price, Max_price_info)
