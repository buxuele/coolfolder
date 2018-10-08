# -*- coding: utf-8 -*-
# info: fanchuang  2018/5/30 22:31
# 目的: 


import os
import time
import re
import requests
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool
from fake_useragent import UserAgent


doors = ['http://www.tu11.com/xingganmeinvxiezhen/list_1_%d.html' % h for h in range(1, 50)]
headers = {'User-Agent': UserAgent().random}
s = requests.Session()
proxies = {'https': '221.228.17.172:8181'}
# proxies2 = {'https': '114.113.126.82:80'}    # 备用代理1
proxies2 = {'https': '113.240.226.164:8080'}     # 备用代理2
pages = 'SexyPages.txt'


# 1. 获取所有的页面链接，保存到 page_url.txt
def getPageUrl(url):
    resp = s.get(url, headers=headers, proxies=proxies2)
    if resp.status_code == 200:
        # print('ok: ' + resp.url)
        soup = BeautifulSoup(resp.text, 'lxml')
        tar = soup.find_all('a', class_='leibie')
        # print(len(tar))

        for t in tar:
            page_url = 'http://www.tu11.com' + t.get('href')
            # print(page_url)

            with open(pages, 'a') as f:
                f.write(page_url + '\n')
    else:
        print('sorry,nothing: ' + str(resp.status_code))


# 2. 根据第一个函数得到的 页面URL来 获取每个每个页面下的第一张图片的 地址，然后再格式化它。
#    这里就是难点了。。。。
def getImgUrl(url):
    # for k in open('hotPages.txt', 'r'):
    # resp = s.get(k.strip(), headers=headers, proxies=proxies)

    resp = s.get(url, headers=headers, proxies=proxies)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'lxml')
        tar = soup.find(src=re.compile('picture')).get('src')
        if tar:
            # print(tar)

            # print(len(tar.split('/')[-1].split('.')[0])) # 2
            # 下面是 如何替换的问题。
            if len(tar.split('/')[-1].split('.')[0]) == 1:
                l = list(tar)
                for i in range(1, 50):
                    l[-5] = str(i)
                    s2 = ''.join(l)
                    # print(s)    #  这里就可以写入文件了
                    with open('hotImgUrls.txt', 'a') as f:
                        f.write(s2 + '\n')

            else:
                taa = tar.replace(tar.split('/')[-1].split('.')[0], '1')
                l = list(taa)
                for i in range(1, 50):
                    l[-5] = str(i)
                    s2 = ''.join(l)
                    # print(s)  # 这里就可以写入文件了
                    with open('hotImgUrls.txt', 'a') as f:
                        f.write(s2 + '\n')


if __name__ == '__main__':
    # 1. 获取所有的页面链接，保存到 page_url.txt
    for d in doors:
        getPageUrl(d)
    time.sleep(2)
    # 2 获取每个每个页面下的第一张图片的 地址，然后再格式化它, 写入 allUrls.txt


    start = time.time()
    print(start)

    urls = [u.strip() for u in open(pages, 'r')]

    pool = Pool(25)
    pool.map(getImgUrl, urls)
    pool.close()
    pool.join()

    print('All done!,  cost time: ')
    print(time.time() - start)





























 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 