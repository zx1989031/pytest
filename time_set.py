#coding:utf8
#python 时间相关函数
import time
#本地时间戳
localtime = time.localtime(time.time())
print localtime

print localtime.tm_hour

#格式化生成时间
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(1532620800))

#格式时间生成时间戳
print time.mktime(time.strptime("2018-07-27","%Y-%m-%d"))

