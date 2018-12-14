# -*- coding: utf-8 -*-

import requests
from lxml import etree

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
    ('keyword', '\u82F9\u679C\u7535\u8111'),
    ('enc', 'utf-8'),
    ('qrst', '1'),
    ('rt', '1'),
    ('stop', '1'),
    ('vt', '2'),
    ('bs', '1'),
    ('wq', '\u82F9\u679C\u7535\u8111'),
    ('ev', 'exbrand_Apple^'),
    ('page', '3'),
    ('s', '31'),
    ('scrolling', 'y'),
    ('log_id', '1544780767.10103'),
    ('tpl', '1_M'),
    ('show_items', '5225346,7629588,24350743428,7629508,4471771,7629548,29625659560,7842699,30112562888,7842691,5225342,4331185,13374931741,8164004,4331183,7842695,24350743427,30112562889,11586487151,29625659561,4331187,11566407039,4331151,4331143,4335021,30380050298,7629614,21235096374,14108281439,14104227569'),
)

response = requests.get('https://search.jd.com/s_new.php', headers=headers, params=params)
tree = etree.HTML(response.text)
skus = tree.xpath('//li[@class="gl-item"]/@data-sku')
for i in skus:
    print(i)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://search.jd.com/s_new.php?keyword=%E8%8B%B9%E6%9E%9C%E7%94%B5%E8%84%91&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&bs=1&wq=%E8%8B%B9%E6%9E%9C%E7%94%B5%E8%84%91&ev=exbrand_Apple%5E&page=2&s=31&scrolling=y&log_id=1544780767.10103&tpl=1_M&show_items=5225346,7629588,24350743428,7629508,4471771,7629548,29625659560,7842699,30112562888,7842691,5225342,4331185,13374931741,8164004,4331183,7842695,24350743427,30112562889,11586487151,29625659561,4331187,11566407039,4331151,4331143,4335021,30380050298,7629614,21235096374,14108281439,14104227569', headers=headers)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BA%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&bs=1&wq=%E5%8D%8E%E4%B8%BA%E6%89%8B%E6%9C%BA&ev=exbrand_%E5%8D%8E%E4%B8%BA%EF%BC%88HUAWEI%EF%BC%89%5E&page=3&s=58&click=0', headers=headers)

