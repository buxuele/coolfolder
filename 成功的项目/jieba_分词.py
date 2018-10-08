# -*- coding: utf-8 -*-
"""
    author: fanchuangwater
    date: 2018/4/6
    time: 17:01
    description: 反正就是尝试不同的库类和方法，多练习代码
"""

import jieba

w = '书上说的话，不可以全都信，但是我可以体会一下。'

seg_list = jieba.cut(w, cut_all=True)
print("全模式: " + '/'.join(seg_list))


