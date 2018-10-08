# -*- coding: utf-8 -*-
# info: fanchuang  2018/5/31 0:32
# 目的: 下载的话，使用 gevent

from gevent import monkey
monkey.patch_all()

import requests
import re
import time
import os
import gevent
from gevent import pool
from fake_useragent import UserAgent


headers = {'User-Agent': UserAgent().random}
s = requests.Session()
proxies = {'https': '221.228.17.172:8181'}
proxies2 = {'https': '113.240.226.164:8080'}  # 备用代理


def justDownload(url):
    filename = url.split('/')[-3] + url.split('/')[-2] + url.split('/')[-1]
    resp = s.get(url.strip(), headers=headers, proxies=proxies2)
    if resp.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(resp.content)

    # else:
    #     pass
    #     # print('sorry!'+ url)


if __name__ == '__main__':
    t1 = time.time()

    os.makedirs('sexygirls', exist_ok=True)
    os.chdir('sexygirls')

    poo = pool.Pool(10)
    jobs = []
    urls = [u.strip() for u in open('h**ls.txt', 'r')]
    for u in urls:
        jobs.append(poo.spawn(justDownload, u))
    gevent.joinall(jobs)

    print('cost time is :  ')
    print(time.time() - t1)
























 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 