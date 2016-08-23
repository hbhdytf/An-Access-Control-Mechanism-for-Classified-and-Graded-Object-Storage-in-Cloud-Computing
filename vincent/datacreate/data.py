#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time
import threading
import datetime
import random
from random import choice
import MySQLdb
#####################
content = os.popen("curl -D- -H 'X-Storage-User:ytf' http://127.0.0.1:8080/auth/v1.0").readlines()
token = content[2].strip()
url = content[1].split(':',1)[-1].strip()
#f = file('./temp.log','w+')
#t = time.strftime('%Y-%m-%d %H:%M:%S')
#f.write(t)
#f.write('\n')
'''for j in range(10,50):
    temp=j
    content = os.popen("curl -X PUT  -H '%s' %s/ytf%s" %(token,url,temp))
'''
name ="圣诚杰安博彬宝斌超盛畅灿纯恩帆福富贵桂瀚豪翰皓弘\
恒海宏洪涵慧荷蕙航嘉俊君峻健和禾佳静娇娟净睛善康坤兰\
岚莲丽立亮伶俪明名铭美宁朋鹏琪芹清晴胜思顺舒森升潭婷\
伟文益宜韵阳运乐怡芸盈园翊智哲志振展忠昭真正雅悦莹娅欣勋轩旭新熙金真"

cls=[]
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='root',db='auth',port=3306)
    cur=conn.cursor()
    count = cur.execute('select seclass_id from TSeclass')
    for c in cur.fetchall():
        cls.append(str(c[0]))
    cur.close()
    conn.close()
except Exception as e:
     print("Mysql Error:",e)
#print("cls :",choice(cls))

temp = 2
for temp in range(3,10):
    for temp1 in range(0,1000):
        filename = "".join(random.sample(name,3))
        content = os.popen("curl -X PUT -T /home/sandy/vincent/1.txt -D- -H 'object_name:%s' -H 'parent_secl_id:%s' -H 'obj_seclevel:4' -H 'Content-Type:audio/mp3' -H '%s' %s/ytf%s/%sytf%s.mp3 " %(filename,choice(cls),token,url,temp,temp,temp1))
        time.sleep(0.05)
#t2 = time.strftime('%Y-%m-%d %H:%M:%S')
#f.write(t2)
#f.write('\n')
#f.close()

