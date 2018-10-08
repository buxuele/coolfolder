import re
import time
import os
import requests
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool

#   
#   重点在于soup.find_all()  的各种有效的用法。
# url = 'http://***.html'
urls = ['http://***531_%s.html' % s for s in range(2, 50)]

headers = {
    'User-Agent': 'Mozi***N) AppleW***64.0.3282.168 Mobile Safari/537.36'
}


# 访问一个网页 ，返回 response
def ask_page(url):
    s = requests.Session()
    page = s.get(url, headers=headers)
    page.encoding = 'utf-8'
    return page


# 找到网页中想要的链接，并返回
def get_link(url):
    page = ask_page(url)
    soup = BeautifulSoup(page.text, 'lxml')
    lis = soup.find_all(href=re.compile("2018-01-23")) # 重点
    for l in lis:
        return l.get("href")

# 下载图片
def download(url):
    link = get_link(url)
    print("正在下载： " + link)# 获取图片的唯一URL
    pic = ask_page(link).content      # 获取图片的内容
    fn = link.split('/')[-1]
    with open(fn, 'wb') as f:
        f.write(pic)


# 单线程下载
# if __name__ == '__main__':
#     os.chdir('大师')
#     start = time.time()
#     for u in urls:
#         download(u)
#     end = time.time()
#     print("下载完成！单线程下载一共消耗的时间是：" + str(end - start))
#     #    下载完成！单线程下载一共消耗的时间是：50.170109033584595


# 多线程下载
if __name__ == '__main__':
    os.mkdir('大师')
    os.chdir('大师')
    start = time.time()

    pool = Pool(20)         # 开20个线程
    pool.map(download, urls)
    pool.close()
    pool.join()

    end = time.time()
    print("下载完成！多线程下载一共消耗的时间是：" +   str(end - start))
# 下载完成！  10 时间是：26.677047729492188
#  下载完成！ 20 时间是：26.300049304962158