

import os
import time
import re
import requests
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool
from fake_useragent import UserAgent


import random
# proxies = {'https': '221.228.17.172:8181'}
# proxies2 = {'https': '114.113.126.82:80'}
# proxies3 = {'https': '113.240.226.164:8080'}


hide = [{'https': '221.228.17.172:8181'},
        {'https': '114.113.126.82:80'},
        {'https': '113.240.226.164:8080'}]



url = 'http:/***/11313.html'

doors = ['http****ist_2_%d.html' % h for h in range(150)]
headers = {'User-Agent': UserAgent().random}
s = requests.Session()
proxies = {'https': '221.228.17.172:8181'}
proxies2 = {'https': '113.240.226.164:8080'}     # 备用代理


resp = s.get(url, headers=headers, proxies=random.choice(hide))
print(resp.status_code)











