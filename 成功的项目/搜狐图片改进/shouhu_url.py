# -*- coding: utf-8 -*-
# author: fanchuangwater  Administrator
# time: 2018/4/29 18:31
# about:

import json
import requests
from fake_useragent import UserAgent
from multiprocessing.dummy import Pool

u = UserAgent()

headers = {
    'User-Agent': u.random
}

def get_articles(url):
    s = requests.Session()
    page = s.get(url, headers=headers)
    w = json.loads(page.json())
    for d in w['data']:
        print('http:' + d['url'])
        with open('fashion.txt', 'a') as f:
            f.write('http:' + d['url'] + '\n')

urls = ['http:***0tY2hhbm5lbEBzb2h1LmNvbQ==&pageNumber=%d&pageSize=10&categoryId=&_=1525493332754' % j for j in range(1, 4)]


my_pool = Pool()
my_pool.map(get_articles, urls)
my_pool.close()
my_pool.join()

#
# for u in urls:
#     get_articles(u)
