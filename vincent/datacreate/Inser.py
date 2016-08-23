#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 加载模块
import sys
import MySQLdb
import datetime

# 设置默认编码为UTF-8，否则从数据库
# 读出的UTF-8数据无法正常显示
reload(sys)
sys.setdefaultencoding('utf-8')
#T = (('1','1','10','1','10','1','atyu30'), ('2','1','10','1','10','1','atyu30'))

# 连接数据库
conn = MySQLdb.Connection(host="localhost", user="root", passwd="root", charset="UTF8")
conn.select_db('auth')

# 创建指针，并设置数据的返回模式为字典
cursor = conn.cursor(MySQLdb.cursors.DictCursor)

for x in range(1001,1000000):
    dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    username = 'ytf'+ str(x)
    phone = str(15600000000+x)
    T=(str(330+x),'','',username,username,username,'5',phone,phone+'@qq.com',dt,None,None)
    #T=('','',username,username,username,'5','15600000330','15600000330@qq.com',dt)
    # 执行SQL
    cursor.execute("insert into TUser values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", T)
    if x % 1000 == 0 :
        conn.commit()
# 关闭指针
cursor.close()

# 关闭数据库连接
conn.commit()
conn.close()

