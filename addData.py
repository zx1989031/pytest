#encoding: utf-8
#!/usr/bin/python
#Filename addData.py
import MySQLdb

#打开数据库链接
db= MySQLdb.connect('localhost','root','a1989031','local_kangshifu_xcx',charset='utf8')

#使用用cursor()方法获取操作游标
cursor = db.cursor()

#使用execute方法执行SQL
cursor.execute('select version()')

#使用fetchone()方法获取一条数据
data = cursor.fetchone()

print "Database version: %s" % data

#关闭数据库链接

