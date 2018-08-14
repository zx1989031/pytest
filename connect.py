#encoding: utf-8
#!/usr/bin/python
#Filename addData.py
import MySQLdb
class conect:
    def __init__(self,host,user,passwd,usedb):
        #链接数据库
        self.db = MySQLdb.connect(host,user,passwd,usedb,charset='utf8')
        self.cursor = self.db.cursor()

    def select(self,sqlData):
        self.cursor.execute(sqlData)
        data = self.cursor.fetchone()

    def addData(self,sqlData):
        try:
            #执行sql语句
            self.cursor.execute(sqlData)
            #提交到数据库执行
            self.db.commit()
        except:
            #rollback in case there is any error
            db.rollback()
    def __del__(self):
        #关闭数据库
        self.db.close()

#实例化链接数据库
db = conect('localhost','root','a1989031','test')
#查询数据
# db.select('select version()')

# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

addsql = """insert into pre_test (name,age)values('zs1',1)"""
res = db.addData(addsql)
print res