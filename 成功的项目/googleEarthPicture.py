from gevent import monkey 
monkey.patch_all()

import requests 
import re 
import time 
import os 
import gevent 
import base64
from gevent import pool

s = requests.Session()


def get_page(url):
    filename = url.split('/')[-1][:4] + '.jpg'
    resp = s.get(url)
    if resp.status_code == 200:
        data = resp.json()
        img_data = data['dataUri'].replace('data:image/jpeg;base64,', '')
        img_cont = base64.b64decode(img_data)

        with open(filename, 'wb') as f:
            f.write(img_cont)

    else:
        print('sorry!')



t1 = time.time()
# os.mkdir('GoogleEarth2')
os.chdir('GoogleEarth2')

poo = pool.Pool(10)
jobs = []

urls = ['https://www.gstatic.com/prettyearth/assets/data/v2/%d.json' % x for x in range(6001, 8000)]

for u in urls:
    jobs.append(poo.spawn(get_page, u))
gevent.joinall(jobs)

print('cost time is :  ')
print(time.time() - t1)