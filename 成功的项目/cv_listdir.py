import os
import cv2


# 此文件可以把 指定文件夹下的所有图片进行操作。
path = ("F://cvX//legs")
k = os.listdir(path)
os.chdir(path)
for i in k:

    img = cv2.imread('{}'.format(i))
    g = cv2.cvtColor(img, 6)
    cv2.imwrite("x"+'{}'.format(i), g)
    # cv2.waitKey(0)
print("done!")
