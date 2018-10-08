# -*- coding: utf-8 -*-
# author: fanchuangwater  Administrator
# time: 2018/4/11 21:03
# description: 

#  最基本的数据库连接

# 1.在连接数据库之前，确保数据库已经新建了数据库，
# 且已经新建了一张表，


import pymysql

db = pymysql.connect('localhost', 'root', '***', 'quotes')
cursor = db.cursor()

cursor.execute("select VERSION()")

data = cursor.fetchone()

print("database version : %s" % data)

db.close()
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 