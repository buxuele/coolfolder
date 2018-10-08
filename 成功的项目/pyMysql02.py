# -*- coding: utf-8 -*-
# author: fanchuangwater  Administrator
# time: 2018/4/11 22:11
# description: 

#  创建一个数据库表

import pymysql

db = pymysql.connect("localhost", "root", "*****", "quotes")

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS GIRLS")

sql = """  
         create table girls(
         name char(20) not null,
         age int,
         payment float); """

cursor.execute(sql)

db.close()
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 