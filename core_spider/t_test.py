# -*- coding: utf-8 -*-

import requests
from lxml import etree

import requests

proxy = {
            "http": 'http://lum-customer-hl_b9fea07e-zone-zone8-dns-remote:8lvtlx73qqnu@zproxy.luminati-china.io:22225',
            "https": 'http://lum-customer-hl_b9fea07e-zone-zone8-dns-remote:8lvtlx73qqnu@zproxy.luminati-china.io:22225'
        }
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
    ('skuIds', 'J_5225346,J_'),
    ('type', '1'),
)

# response = requests.get('https://p.3.cn/prices/mgets', headers=headers, params=params, proxies=proxy)
response = requests.get("https://www.baidu.com", proxies=proxy, timeout=5)
print(response.content)


#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://search.jd.com/s_new.php?keyword=%E8%8B%B9%E6%9E%9C%E7%94%B5%E8%84%91&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&bs=1&wq=%E8%8B%B9%E6%9E%9C%E7%94%B5%E8%84%91&ev=exbrand_Apple%5E&page=2&s=31&scrolling=y&log_id=1544780767.10103&tpl=1_M&show_items=5225346,7629588,24350743428,7629508,4471771,7629548,29625659560,7842699,30112562888,7842691,5225342,4331185,13374931741,8164004,4331183,7842695,24350743427,30112562889,11586487151,29625659561,4331187,11566407039,4331151,4331143,4335021,30380050298,7629614,21235096374,14108281439,14104227569', headers=headers)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BA%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&bs=1&wq=%E5%8D%8E%E4%B8%BA%E6%89%8B%E6%9C%BA&ev=exbrand_%E5%8D%8E%E4%B8%BA%EF%BC%88HUAWEI%EF%BC%89%5E&page=3&s=58&click=0', headers=headers)

