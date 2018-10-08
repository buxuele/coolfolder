# -*- coding: utf-8 -*-
# author: fanchuangwater  Administrator
# time: 2018/4/10 19:31
# description:
# 对于单纯的识别条形码：pip3 install zxing


import zxing


reader = zxing.BarCodeReader()
barcode = reader.decode('ean13.png')

print(barcode)
print(barcode.raw)

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 