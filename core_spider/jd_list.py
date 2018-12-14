# -*- coding: utf-8 -*-

import requests
from configs.config import logger
from lxml import etree
from tools.mongo_tools import Mongo_db

import time

class List_spider():

    def __init__(self, keyword, page):

        self.mongo = Mongo_db()
        self.keyword = keyword
        self.page = page
        self.item = []

    def search(self, page):

        headers = {
            'authority': 'search.jd.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3409.2 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': '__jdu=641087548; shshshfpb=05b1d1356646c036716a9d081e5a941ab82f8b57093c59abb5b7146b41; PCSYCityID=1381; shshshfpa=9f92e083-fd26-5ffd-5c7a-73b803f1db6b-1544410462; xtest=299.cf6b6759; ipLoc-djd=1-72-2799-0; unpl=V2_ZzNtbRAHEBwiWxVcK01bUmICEVoSAxQddAoSUisYXwUyAhVeclRCFXwURldnGV4UZwUZX0tcQhRFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2U34ZXQxhBxdUcmdEJUU4Q1V5GFQHVwIiXHIVF0l3DkBdfRoRAmIDE1REU0YcRQl2Vw%3d%3d; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_cab8fbb9ae6f4026aef903e7a021d062|1544693885422; qrsc=3; 3AB9D23F7A4B3C9B=UDR2LAGT36DXD5KCJPLCFWCQGTDG4UHPX2PYHB3HXCUE2DJV36UC54M6MPGTBIYHG5YBR4EKWQJHRV34GM6E7F7HJI; _gcl_au=1.1.1695706138.1544759275; __jdc=122270672; user-key=3106e820-a4cd-4e43-8f0a-f4df1e03f89d; cn=0; rkv=V0100; __jda=122270672.641087548.1544410460.1544759275.1544773679.5; shshshfp=f15ef1e4c531cad5fbd858cc101b0aef; __jdb=122270672.23.641087548|5.1544773679; shshshsID=80aad8ac54e1907cb0928174e90ef898_22_1544777606439',
        }

        params = (
            ('keyword', self.keyword),
            ('enc', 'utf-8'),
            ('wq', self.keyword),
            ('page', page),
            ('click', '0'),
        )

                # search_url1 = 'https://search.jd.com/Search?keyword={key}&enc=utf-8&page={page}'
        response = requests.get('https://search.jd.com/Search', headers=headers, params=params)
        if not response:
            return None
        return response.text

    def search_half(self, page):
        """加载另外一半数据"""
        headers = {
            'cookie': '__jdu=641087548; shshshfpb=05b1d1356646c036716a9d081e5a941ab82f8b57093c59abb5b7146b41; PCSYCityID=1381; shshshfpa=9f92e083-fd26-5ffd-5c7a-73b803f1db6b-1544410462; xtest=299.cf6b6759; ipLoc-djd=1-72-2799-0; qrsc=3; __jdc=122270672; user-key=3106e820-a4cd-4e43-8f0a-f4df1e03f89d; cn=0; rkv=V0100; __jda=122270672.641087548.1544410460.1544759275.1544773679.5; shshshfp=f15ef1e4c531cad5fbd858cc101b0aef; unpl=V2_ZzNtbRJQF0B2WBFSK01VDGICEgpLVhERdAhOB31JCVZhARIOclRCFXwURldnGVkUZwUZWEZcRx1FCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2U34ZXQxhBxdUcmdEJUU4RFV7EF4EVwIiXHIVF0l1Dk9cfBsRAmIDE1REU0YcRQl2Vw%3d%3d; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_a6ed2af7ae88401f80c5019b7adb731b|1544780761481; __jdb=122270672.37.641087548|5.1544773679; shshshsID=80aad8ac54e1907cb0928174e90ef898_36_1544780769982; 3AB9D23F7A4B3C9B=UDR2LAGT36DXD5KCJPLCFWCQGTDG4UHPX2PYHB3HXCUE2DJV36UC54M6MPGTBIYHG5YBR4EKWQJHRV34GM6E7F7HJI',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3409.2 Safari/537.36',
            'accept': '*/*',
            'referer': 'https://search.jd.com/Search?keyword=%E8%8B%B9%E6%9E%9C%E7%94%B5%E8%84%91&enc=utf-8&wq=%E8%8B%B9%E6%9E%9C%E7%94%B5%E8%84%91&pvid=28ceab45ed5a491cb42565741a378e7e',
            'authority': 'search.jd.com',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = (
            ('keyword', self.keyword),
            ('enc', 'utf-8'),
            ('qrst', '1'),
            ('rt', '1'),
            ('stop', '1'),
            ('vt', '2'),
            ('bs', '1'),
            ('wq', self.keyword),
            ('page', page),
            ('scrolling', 'y'),
            ('tpl', '1_M'),
            ('show_items', ",".join(self.item))
             )

        response = requests.get('https://search.jd.com/s_new.php', headers=headers, params=params)
        self.item = []  # 置空列表数据
        return response.text


    def list_resume(self, html):
        """解析出商品id page"""

        tree = etree.HTML(html)
        skus = tree.xpath('//li[@class="gl-item"]/@data-sku')
        for i in skus:
            self.item.append(i)  # 添加到列表中
            self.mongo.insert({"sku_id": f"{i}", "sku_search_name": f"{self.keyword}", "search_time": int(time.time())})
            time.sleep(0.01)



    def run(self):
        logger.info(f"search_run_start:{self.keyword, self.page}")
        for page in range(self.page):
            page_1 = page * 2 + 1  # 从0开始计数 (1,2) (3,4)
            page_2 = page_1 + 1
            time.sleep(1)
            res = self.search(page_1)
            self.list_resume(res)
            res = self.search_half(page_2)
            self.list_resume(res)




if __name__ == '__main__':
    l = List_spider("华为手机", 10)
    l.run()