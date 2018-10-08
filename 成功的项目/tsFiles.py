# -*- coding: utf-8 -*-
# author: fanchuangwater  Administrator
# time: 2018/5/10 23:59
# about: 


import re
import subprocess
import uuid
import requests
from multiprocessing.dummy import Pool

video_url = ''

url = 'http://***.m3u8'
filename = url.split('/')[-1]
mp4_name = filename.split('.')[0]


# 总想把前2个方法合成一个，目前是不行的。
def get_m3u8File(url):
    res = requests.get(url).content
    with open(filename, 'wb') as f:
        f.write(res)


def get_tsFile():
    for i in open(filename, 'r'):
        if i.strip()[0] != '#':
            
            ts_url = 'http://play.caobb-cloudflare.com:6789' + i.strip()
            # print(ts_url)
            # yield ts_url
            ts = requests.get(ts_url).content
            with open(ts_url.split('/')[-1], 'wb') as g:
                g.write(ts)


if __name__ == '__main__':
    # get_m3u8File(url)
    # get_tsFile()

    # print("got all ts !")
    #
    cmd1 = 'copy /b *.ts {}.ts '.format(mp4_name)
    cmd2 = 'ffmpeg -i {0}.ts -vcodec copy -acodec copy {1}.mp4 '.format(mp4_name, mp4_name)
    cmd3 = 'del *.ts'
    cmd4 = 'del *.m3u8'

    # subprocess.call(cmd1, shell=True)
    # subprocess.call(cmd2, shell=True)
    #
    subprocess.call(cmd3, shell=True)
    subprocess.call(cmd4, shell=True)
    # print('got mp4')































 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 