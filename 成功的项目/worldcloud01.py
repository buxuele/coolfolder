# -*- coding: utf-8 -*-
# author: fanchuangwater  Administrator
# time: 2018/4/11 23:13
# description: 
 
from wordcloud import WordCloud
import matplotlib.pyplot as plt

filename = open("story.txt", 'r').read()
wc = WordCloud(background_color='white', width=1000, height=860, margin=2).generate(filename)

plt.imshow(wc)
plt.axis("off")
plt.show()
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 