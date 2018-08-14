#conding:utf8
#/usr/bin/python
#fileName:testgetattr.py
class Test:
    name='zx'
    def __init__(self):
        pass
    def test(self):
        print 'test'
    def hello(self):
        print 'hello'




obj = Test()

#print obj.name
#obj.hello()

# hello =getattr(obj,'test')

methodList = [method for method in dir(obj) if callable(getattr(obj,method))]

print dir(obj)
print methodList








