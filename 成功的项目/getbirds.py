import os
import time
import requests
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool

url = 'http***ge/3'
detail = []
img = []


def ask_page(url):
    s = requests.Session()
    resp = s.get(url)
    # print(resp.status_code, resp.encoding)  #200 UTF-8
    soup = BeautifulSoup(resp.text, 'lxml')
    return soup


def gan(url):
    sou = ask_page(url)
    h = sou.find_all('img')
    for g in h:
        # 52
        if len(g['src']) == 52:
            # print(g['src'])
            img.append(g['src'])
    # print(img)
    return img


def clean_page(url):
    soup = ask_page(url)
    all_a = soup.find_all('h3')   # len= 11
    # print(all_a, len(all_a))
    for i in all_a:
        u = str(i)[13:46]
        detail.append(u)
    detail.pop()
    # print(detail, len(detail))
    return detail


def down(mm):
    pic = requests.get(mm).content
    filename = mm[-11:]
    print(filename)
    time.sleep(2)
    with open(filename, 'wb') as f:
        f.write(pic)


os.mkdir('bilibili')
os.chdir('bilibili')
if __name__ == '__main__':
    st = time.time()
    print(st)

    ml = clean_page(url)
    # print(ml)
    for m in ml:
        ga = gan(m) 	# gan 是一个列表
        pool = Pool(40)
        pool.map(down, ga)
        pool.close()
        pool.join()
        # for mm in ga:
        #     down(mm)

    print("finish time is : ")
    print(time.time()-st)   # 230.4424011707306

#  pool = 20 , time = 117.54977607727051
#  pool = 40 , time =  66.51862406730652
#  pool = 60 , time =


