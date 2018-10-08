# -*- coding: utf-8 -*-
# info: fanchuang  2018/5/20 19:35
# 目的: 


import os
import time
import re
import click
import asyncio
import aiohttp


# url = 'ht****6816726462&pid=hp'

TODAY = time.strftime('%Y-%m-%d', time.localtime(time.time()))
PATTERN = re.compile(r'')

async def getPic(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            json_file = await resp.json()
            data = json_file['images']
            for d in data:
                pic_url = 'https://cn.bing.com' + d['url']
                click.echo(pic_url)

        async with session.get(pic_url) as res:
            with open(pic_url.split('/')[-1], 'wb') as f:
                cont = await res.read()
                f.write(cont)


if __name__ == '__main__':
    os.makedirs('必应壁纸', exist_ok=True)
    os.chdir('必应壁纸')
    loop = asyncio.get_event_loop()
    urls = ['https:**=js&idx=%d&n=1&nc=1526823492560&pid=hp' % x for x in range(7)]
    tasks = [getPic(url) for url in urls]
    loop.run_until_complete(asyncio.gather(*tasks))

    # print(TODAY)




















 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 