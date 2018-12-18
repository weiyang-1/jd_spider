# -*- coding: utf-8 -*-

import requests
from lxml import etree
import json
from tools.mongo_tools import Mongo_db
import time
import datetime
from configs.config import logger


"""京东价格接口：https://p.3.cn/prices/mgets?skuIds=J_5225346,J_&type=1
   京东评论接口：http://club.jd.com/productpage/p-1397092632-s-0-t-3-p-0.html
"""
DATE = datetime.datetime.now().strftime('%Y-%m-%d')
SERVER_JUN_URL = "http://sc.ftqq.com/SCU37154T6493d663e2f8d5bccb44ee60986abb0c5c08f47d89024.send"
def send_2_me(text, desp):
    r = requests.post(SERVER_JUN_URL, data={'text': text, 'desp': desp})
    print(r.status_code)
    print("告诉手机成功")

class JD_Spider():

    def __init__(self, sku_id):
        self.text = ""
        self.desp = ""
        self.sku_id = sku_id
        self.sku_infos = {}
        self.comments_info = {}
        self.mongodb = Mongo_db()
        self.sku_infos["comment_info"] = self.comments_info
        # 设置代理ip
        self.proxy = {
            "http": 'http://lum-customer-hl_b9fea07e-zone-zone8-dns-remote:8lvtlx73qqnu@zproxy.luminati-china.io:22225',
            "https": 'http://lum-customer-hl_b9fea07e-zone-zone8-dns-remote:8lvtlx73qqnu@zproxy.luminati-china.io:22225'
        }

    def get_goods_name(self):
        headers = {
            'authority': 'item.jd.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3409.2 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': 'unpl=V2_ZzNtbUcFExdzC0JSeRpZA2IBE1gSXxQXdA8TV34YCVBkUxVbclRCFXwURldnGV0UZwIZWUdcQxNFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2U34ZXQxhBxdUcmdEJUU4RlN%2bEFgHVwIiXHIVF0lwDUddchERAmIDE1REU0YcRQl2Vw%3d%3d; __jda=122270672.641087548.1544410460.1544410460.1544410461.1; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_4ca3725732474304a9f306d240dd2a67|1544410461241; __jdc=122270672; __jdu=641087548; shshshfpb=05b1d1356646c036716a9d081e5a941ab82f8b57093c59abb5b7146b41; PCSYCityID=1381; shshshfpa=9f92e083-fd26-5ffd-5c7a-73b803f1db6b-1544410462; ipLoc-djd=1-72-2799-0; 3AB9D23F7A4B3C9B=UDR2LAGT36DXD5KCJPLCFWCQGTDG4UHPX2PYHB3HXCUE2DJV36UC54M6MPGTBIYHG5YBR4EKWQJHRV34GM6E7F7HJI; shshshfp=b2c784be4c03871428d26e05fb892653; _gcl_au=1.1.2080295640.1544410498; shshshsID=7be040525e92bbd33b890f5ad7fc93b4_14_1544410778056; __jdb=122270672.14.641087548|1.1544410461',
            'if-modified-since': 'Mon, 10 Dec 2018 02:59:10 GMT',
        }

        # response = requests.get('https://item.jd.com/5225346.html', headers=headers)
        response = requests.get(f'https://item.jd.com/{self.sku_id}.html', headers=headers)
        with open("../datas/comment.html", "w", errors="ignore") as f:
            f.write(response.text)
        tree = etree.HTML(response.text)
        name = tree.xpath('//div[@class="sku-name"]')[0].xpath('string(.)').strip()
        return name

    def get_price(self):

        headers = {
            'Host': 'p.3.cn',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3409.2 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
        }

        params = (
            ('skuIds', f'J_{self.sku_id},J_'),
            ('type', '1'),
        )
        response = ""
        for _ in range(5):
            try:
                response = requests.get('https://p.3.cn/prices/mgets', headers=headers, params=params, proxies=self.proxy, timeout=15)
            except Exception as e:
                logger.error(e)
                time.sleep(10)
                continue
            if "id" in response.text:
                break
        logger.info(response.text)
        res_json = json.loads(response.text)
        try:
            price = res_json[0].get("p", "")
        except:
            price = ""
        try:
            price_plus = res_json[0].get("tpp", "")
        except:
            price_plus = ""
        return price, price_plus
        # """[{"op":"6928.00","m":"9888.00","id":"J_5225346","p":"6488.00","up":"tpp","tpp":"5999.00"}]"""

    def get_comments(self):
        """获取评论数"""
        # https://club.jd.com/comment/productCommentSummaries.action?referenceIds=762958

        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3409.2 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        params = (
            ('referenceIds', self.sku_id),
        )
        response = requests.get('https://club.jd.com/comment/productCommentSummaries.action', headers=headers,
                                params=params)
        print(response.text)
        try:
            res_json = json.loads(response.text)["CommentsCount"][0]
        except:
            res_json = None
        if not res_json:
            return self.comments_info
        self.comments_info["CommentCount"] = res_json["CommentCount"]
        self.comments_info["GoodCount"] = res_json["GoodCount"]
        self.comments_info["GoodRate"] = res_json["GoodRate"]
        self.comments_info["PoorCount"] = res_json["PoorCount"]
        self.comments_info["PoorRate"] = res_json["PoorRate"]
        return self.comments_info


    def run(self):
        # name = self.get_goods_name()
        # time.sleep(1)
        p1, p2 = self.get_price()
        # time.sleep(1)
        # self.get_comments()
        # self.sku_infos["name"] = name
        # 价格设置为列表
        self.sku_infos[f"p1-{DATE}"] = float(p1) if p1 else 0
        self.sku_infos[f"p2-{DATE}"] = float(p2) if p2 else 0
        query = {"sku_id": f"{self.sku_id}"}
        self.mongodb.update(query, self.sku_infos)

def debug():
    # m = Mongo_db()
    # res = m.search({})
    # for i in res:
    #     sku_id = i.get("sku_id", "")
    #     if not sku_id:
    #         continue
    #     print(sku_id)
    jd = JD_Spider(29044581674)
    # jd.get_goods_name()
    # jd.get_comments()
    p1, p2 = jd.get_price()
    print(p1, p2)
    time.sleep(1)
    # 价格设置为列表
    jd.sku_infos[f"p1-{DATE}"] = float(p1) if p1 else 0
    jd.sku_infos[f"p2-{DATE}"] = float(p2) if p2 else 0
    query = {"sku_id": f"{jd.sku_id}"}
    jd.mongodb.update(query, jd.sku_infos)

if __name__ == '__main__':
    # m = Mongo_db()
    # res = m.search({})
    # for i in res:
    #     sku_id = i.get("sku_id", "")
    #     if not sku_id:
    #         continue
    #     jd = JD_Spider(sku_id)
    #     jd.run()
    debug()
