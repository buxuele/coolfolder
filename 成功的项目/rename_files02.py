# -*- coding: utf-8 -*-
# author: fanchuangwater  Administrator
# time: 2018/4/21 20:28
# description: 批量重命名文件


import os

path_name = input("Your file path: ")


def rename_files(path_name):
    i = 0
    all_file = os.listdir(path_name)

    for a in all_file:
        print(a)

        old_file = os.path.join(path_name, a)
        print(old_file)

        b = str(i) + a[-4:]
        print(b)

        new_file = os.path.join(path_name, b)
        print(new_file)

        os.rename(old_file, new_file)
        print('***************')
        i = i + 1


rename_files(path_name)











































 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 