#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time
import random
import datetime
from swiftclient import client
from random import choice
import MySQLdb
import sys
num = int(sys.argv[1])*100
print("from:",num)
if num==0:
    fromnum = 13
    tonum = 100
else:
    fromnum = num
    tonum = num+100


content = os.popen("curl -D- -H 'X-Storage-User:ytf' http://192.168.119.150:8080/auth/v1.0").readlines()
token = content[2].split(':',1)[-1].strip()
#print(token)
url = content[1].split(':',1)[-1].strip()
name ="圣诚杰安博彬宝斌超盛畅灿纯恩帆福富贵桂瀚豪翰皓弘\
恒海宏洪涵慧荷蕙航嘉俊君峻健和禾佳静娇娟净睛善康坤兰\
岚莲丽立亮伶俪明名铭美宁朋鹏琪芹清晴胜思顺舒森升潭婷\
伟文益宜韵阳运乐怡芸盈园翊智哲志振展忠昭真正雅悦莹娅欣勋轩旭新熙金真"

cls=[]
ers=[]
time1 = datetime.datetime.now()
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
cc=''
#print(cls)
for temp in range(fromnum,tonum):
    for temp1 in range(0,1000):
        try:
            if temp1 == 200 :
                time.sleep(1)
            filename = "".join(random.sample(name,3))
            #print(filename)
            cc = choice(cls)
            str1 = client.put_object(url,token,'ytf%s' % temp,'%sytf%s.mp3' % (temp,temp1),'re\n',headers={'object_name':filename,'parent_secl_id':cc, 'obj_seclevel':'4','Content-Type':'audio/mp3',})
            #print(str1)
        except Exception as e:
            try:            
                str1 = client.put_object(url,token,'ytf%s' % temp,'%sytf%s.mp3' % (temp,temp1),'re\n',headers={'object_name':filename,'parent_secl_id':choice(cls), 'obj_seclevel':'4','Content-Type':'audio/mp3',})
            except Exception as e1:
                print('cccccc:,',cc)
                print(e1)
                ers.append(str(e1).split(' ')[3].split('/')[-1])
            #print("round1:",e)

print(ers)
time2 = datetime.datetime.now()
print("------------------")
print("time:",((time2-time1).seconds))
'''
for x in ers:
    try:
        filename = "".join(random.sample(name,3))
        temp,temp1 = x.split('ytf')
        str1 = client.put_object(url,token,'ytf%s' % temp,'%sytf%s.mp3' % (temp,temp1),'re\n',headers={'object_name':filename,'parent_secl_id':choice(cls), 'obj_seclevel':'4','Content-Type':'audio/mp3',})
        ers.pop(x)
    except Exception as e3:
        print("--els--:%s,%s" % (x,str(e3)))
'''
