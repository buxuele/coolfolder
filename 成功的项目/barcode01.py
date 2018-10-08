# -*- coding: utf-8 -*-
# author: fanchuangwater  Administrator
# time: 2018/4/9 19:40
# 目的：尝试写一个条形码的识别脚本
# 原则： 以自己的目的为出发点。
# 此篇包含2部分。1是识别出条形码代表的数字。2是 生成条形码（等机会再说吧）
# 顺序：原图/灰度/梯度/模糊/


# 未完成的部分：
# 1.核心工功能是完全偏离了，此篇只是练习了代码而已。
# 2 下一步是把这篇的功能来封装一下。
# 3.然后是识别，读取隐藏的数字内容

import os
import cv2
import numpy as np

# 1 图片初步处理
img = cv2.imread("b.jpg", 1)
# print(img.size)
# print(img.shape)
img = cv2.resize(img, (600, 800))
cut = img.copy()[0:600, 0:600]         # 截取图片的一部分。
gray = cv2.cvtColor(cut, cv2.COLOR_BGR2GRAY)

# 2.通过梯度检测出 图片中 条形码的位置
# 引用：索贝尔算子（Sobel operator）主要用作边缘检测，在技术上，它是一离散性差分算子，用来运算图像亮度函数的灰度之近似值。在图像的任何一点使用此算子，将会产生对应的灰度矢量或是其法矢量
gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)

gradient = cv2.subtract(gradX, gradY)
gradient = cv2.convertScaleAbs(gradient)

# 3.下一步是去噪，把模糊后的图片二值化。
# 第一个255，是小于等于255的像素设置为0， 其余的设为255（即为第二个255）
# 0 是纯黑， 255是纯白
blurred = cv2.blur(gradient, (9, 9))
(_, thresh) = cv2.threshold(blurred, 205, 255, cv2.THRESH_BINARY)     # 这里的205作为阈值，要随时调整


# 4.进一步去除可能的斑点
# kernel, 构造一个长方形的内核，21是宽度，7是长度，用来消除缝隙
# morphologyEx，形态学操作，也是为了去除竖杠间的缝隙
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# 5.如果还有斑点的话，可以继续来消除 腐蚀和膨胀操作
erode = cv2.erode(closed, None, iterations=4)
dilate = cv2.dilate(erode, None, iterations=4)



# 6.核心难点在于这个找轮廓，画轮廓
# 6.1找轮廓：原图/灰度/阈值/轮廓 。cv2.findContours
_x, contours, hierarchy = cv2.findContours(dilate.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# c = sorted(contours, key=cv2.contourArea())

# 6.2画轮廓：cv2.drawContours 原图， 哪个哪些轮廓（是一个列表）， 第几个轮廓（-1,是全都画上），颜色，粗度

# 6.2.1画轮廓的第一种做法：从contours[0] 到contours[1] 一直找（尝试）下去看看哪一个是想要的，本例中是1
# 是可行的, 也是基本的用法
# cnt = contours[1]
# cv2.drawContours(cut, [cnt], 0, (0, 255, 0), 3)

# 6.2.2画轮廓的第2种做法：高级用法，完善用法,但是在我这里还是失败了
# 这个c 就是我们想要的，那个条形码所在的轮廓
# 默认的contours是按照小到大的顺序，这个反转是Ture，变成从大到小
c = sorted(contours, key=cv2.contourArea, reverse=True)[0]
# 根据轮廓找最小矩形，另外有 cv2.minEnclosingCircle().外接圆
rect = cv2.minAreaRect(c)
# 这个box 是矩形四个角的位置， cv2.boxPoints（）就是来获取这4个位置的
box = np.int_(cv2.boxPoints(rect))
cv2.drawContours(cut, [box], -1, (0, 255, 0), 3)

# 6.2.3画轮廓的第3种做法，自己结合以上来写一个可以行的，改进1的方法
# 其实是只是把教程中的这个np.int0() 改为np.int_()，即可正常运行。
# 所以啊,numpy是图像操作的基础，是底层。


# 7.显示 查看 调整部分
# cv2.imshow("original", img)
cv2.imshow("cut", cut)
# cv2.imshow("graystyle", gray)
# cv2.imshow("gradientstyle", gradient)
# cv2.imshow("blurredstyle", blurred)
# cv2.imshow("threshed", thresh)

# cv2.imshow("closedstyle", closed)
# cv2.imshow("erode", erode)
cv2.imshow("dilate", dilate)


cv2.waitKey(0)
cv2.destroyAllWindows()




  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 