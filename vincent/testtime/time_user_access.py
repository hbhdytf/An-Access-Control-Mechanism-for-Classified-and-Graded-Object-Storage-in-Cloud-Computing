#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time
import random
import datetime
from swiftclient import client
import threading
'''
if raw_input("restart swift or not (y/n):")=='y':
    for k in os.popen('sudo python setup.py install').readlines():
        pass
    for j in os.popen('sudo swift-init main restart').readlines():
        pass
#    print j,
#    time.sleep(0.02)
'''
sumt=0
def test(u,t,t1):
    #print "---",datetime.datetime.now()
    st = datetime.datetime.now()
    for x in xrange(t1):
        try:       
            client.get_object(u,t,"zjj" ,"1.mp3" )
        except:
            pass
    fi = datetime.datetime.now()
    global sumt
    sumt = sumt + ((fi-st).microseconds/1000.000+((fi-st).seconds)*1000)
   #print "***",datetime.datetime.now()

#name = raw_input("Please input the name(for token):")
name = 'cloudms'
while not name:
    name = raw_input("Please input the name(for token):")
if name == "Admin" or name == "sandy":
    content = os.popen("curl -D- -H 'X-Storage-User:%s' -H 'X-Storage-Pass:admin' http://127.0.0.1:8080/auth/v1.0" %name).readlines()
else:
    content = os.popen("curl -D- -H 'X-Storage-User:%s' http://127.0.0.1:8080/auth/v1.0" %name).readlines()
token = content[2].strip()
url = content[1].split(':',1)[-1].strip()
#for i in content:
#    print i,
#    time.sleep(0.3)
#print token

#getmethod = os.popen("curl -k -X GET -H '%s' %s" %(token,url)).readlines()
#for dd in getmethod:
#    print dd,
#    time.sleep(0.3)
geturl = '/'.join([url,'zjj/'])
#print "curl -X GET -H '%s' %s"%(token,geturl)
#print "curl -X PUT -T ./1.txt -D- -H 'object_name:小酒窝' -H 'parent_secl_id:7' -H 'obj_seclevel:4' -H 'Content-Type:audio/mp3' -H '%s' %s" %(token,url)
t1 = 50
t2 = 10
token = token.split(": ")[-1]
global sum 
sum = 0
r = random.randint(1,104)
#str1 = "curl -s -X GET -H '%s' %s/ytf%s/%sytf%s.txt"%(token,url,r,r,random.randint(1,10000))
try:
    #str1=client.get_object(url,token,"ytf%s" % r,"%sytf%s.txt" % (r,random.randint(1,10000)))
    #str1=client.get_object(url,token,"zjj" ,"1.mp3" )
    #print str1
    print '-'*63
    #print '+',' '*18,'Meta Data Information',' '*18,'+'
    print '+',format('Meta Data Information',"^59"),'+'
    print '-'*63
    meta=client.head_object(url,token,"zjj" ,"1.mp3" )
    for item,value in meta.items():
        if "object_name" in item:
            print '+',format(item,'<20'),'+',format(value,'<39'),'+'
        else:
            print '+',format(item,'<20'),'+',format(value,'<36'),'+'
    print '-'*63
    #print meta
    
except Exception as e:
    print e
print 
print '+',format('Time by Stress Test',"^59"),'+'
#print ""
print


threadpool=[]
for i in xrange(t2):
    th = threading.Thread(target = test,args = (url,token,t1))
    threadpool.append(th)
time1 = datetime.datetime.now()

#---------------NOW PRINT RUNING TIMESTAMP----------
#print "\033[32;40m"
print '-'*63
print "+ Starting Thread Stress Testing: \t+",time1.strftime('%Y-%m-%d %H:%M:%S'),"+"

for th in threadpool:
    th.start()
for th in threadpool:
    threading.Thread.join(th)
'''
for y in range(t1):
    for x in range(t2):
        r = random.randint(1,104)
        try:
            client.get_object(url,token,"ytf%s" % r,"%sytf%s.txt" % (r,random.randint(1,10000)))
        except:
            pass
'''
time2 = datetime.datetime.now()

#---------------NOW PRINT RUNING TIMESTAMP----------

#print "+ Starting Process Stress Testing: \t+",time2.strftime('%Y-%m-%d %H:%M:%S'),'+'

time3 = datetime.datetime.now()
req = 10
for x in xrange(req):
    try:
        str1 = client.get_object(url,token,"zjj" ,"1.mp3" )
    except Exception as e:
        #print e
        pass
time4 = datetime.datetime.now()

#---------------NOW PRINT RUNING TIMESTAMP----------
print "+ All Stress Testing Finished: \t\t+",time4.strftime('%Y-%m-%d %H:%M:%S'),"+"
print '-'*63
time.sleep(0.5)
print
#print
#print time2
#print (time2-time1).microseconds
#print "Runing Time : %ss" % (int((time2-time1).seconds)+int((time4-time3).seconds))
print '+',format("Runing Time : %ss" % (int((time2-time1).seconds)+int((time4-time3).seconds)),"^59"),'+'
#print '+',format("Requests Num: %s" % req,"^59"),'+'
print '\033[1;31;40m'
print '*' * 63
print format("OpenStack Swift Url:",'<29'),url
print format("Access User Name:",'<29'),name 
#print format("Requests Num:",'<29'),req
print format("Thread Parallel Num:",'<29'),(t2*t1)
#print format("Average access time(Thread):",'<29'),((time2-time1).microseconds/1000.000+((time2-time1).seconds)*1000)/(t1),"ms"
print format("Average access time:",'<29'),(sumt)/(t1*t2),"ms"
#print format("Average access time(Thread):",'<29'),(sumt)/(t1*t2),"ms"
#print format("Average access time(Process):",'<29'),((time4-time3).microseconds/1000.000+((time4-time3).seconds)*1000)/req,"ms"
#print "File Numbers:\t\t","1049948"
print '*' * 63,'\033[0m'
