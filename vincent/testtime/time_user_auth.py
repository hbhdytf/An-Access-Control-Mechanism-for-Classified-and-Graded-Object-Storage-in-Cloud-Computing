#!/usr/bin/env python # -*- coding:utf-8 -*-
import os
import time
import random
import datetime
from swiftclient import client
import threading
def test(t1):
    #print "---",datetime.datetime.now()
    for x in xrange(t1):
        try:       
            name = "ytf%s" % random.randint(1,1000000)
            os.popen("curl -D- -H 'X-Storage-User:%s' http://127.0.0.1:8080/auth/v1.0" % name).readlines()
        except:
            pass
    #print "***",datetime.datetime.now()
t1 = 20 
t2 = 100
global sum 
sum = 0
threadpool=[]
for i in xrange(t2):
    th = threading.Thread(target = test,args = (t1))
    threadpool.append(th)
time1 = datetime.datetime.now()
print time1
for th in threadpool:
    th.start()
for th in threadpool:
    threading.Thread.join(th)
time2 = datetime.datetime.now()

time3 = datetime.datetime.now()
for x in range(1,1000):
    try:
        test(1)
    except Exception as e:
        #print e
        pass
time4 = datetime.datetime.now()

print time2
print (time2-time1).microseconds
print (time2-time1).seconds
print '\033[1;31;40m'
print '*' * 50
print "Average access time(Thread):\t",((time2-time1).microseconds/1000.000+((time2-time1).seconds)*1000)/(t1*t2),"ms"
print "Average access time(Process):\t",((time4-time3).microseconds/1000.000+((time4-time3).seconds)*1000)/1000,"ms"
#print "File Numbers:\t\t","1049948"
print '*' * 50
print '\033[0m'
