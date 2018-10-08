# -*- coding: utf-8 -*-
# author: fanchuangwater  Administrator
# time: 2018/5/2 21:01
# about: 写一个自己经常会用到的 定时器
# 用起来还是很简洁的。另外，需要计算好 相隔多长时间来做这个任务。

import datetime
import time
from threading import Timer


def shitTodo():
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def myTimer():
    timer = Timer(5, shitTodo, ()).start()


if __name__ == '__main__':
    # shitTodo()
    myTimer()





















 
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 