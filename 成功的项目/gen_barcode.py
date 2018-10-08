# -*- coding: utf-8 -*-
# author: fanchuangwater  Administrator
# time: 2018/4/10 20:10

# description: 对于单纯的生成条形码： pip install pyBarcode

import barcode
from barcode.writer import ImageWriter

# 生成 .png 格式的条形码
png = barcode.get('ean13', '123456789102', writer=ImageWriter())
fn = png.save('ean13')

# 生成 .svg 格式的条形码
svg = barcode.get('ean13', '123456789102')
fm = svg.save('ean13')
fm2 = svg.save('ean14')


  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 