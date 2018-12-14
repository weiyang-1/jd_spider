# -*- coding: utf-8 -*-

from core_spider.jd_goods_details import JD_Spider
from core_spider.jd_list import List_spider
from tools.mongo_tools import Mongo_db

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

run()