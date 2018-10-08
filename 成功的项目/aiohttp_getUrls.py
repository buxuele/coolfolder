# -*- coding: utf-8 -*-
# author: fanchuangwater  Administrator
# time: 2018/5/18 20:57
# about: 

import asyncio
import aiohttp
import time
import simplejson
from fake_useragent import UserAgent


u = UserAgent()
headers = {
    'User-Agent': u.random
}


async def get_articles(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            page = await resp.json()    # 这里的page是 json 格式的文件

            w = simplejson.loads(page)
            # print(type(w))

            for d in w['data']:
                print('http:' + d['url'])
                with open('aithttp_way.txt', 'a') as f:
                    f.write('http:' + d['url'] + '\n')


urls = [
    'http://***Dg2N0Bz***ryId=&_=1526648009351' % j
    for j in range(1, 30)]

t1 = time.time()

loop = asyncio.get_event_loop()
tasks = [get_articles(url) for url in urls]
loop.run_until_complete(asyncio.gather(*tasks))

print(time.time() - t1)     # 0.5710327625274658
# multiprocessing   0.8040459156036377
# 0.5240302085876465
























 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 