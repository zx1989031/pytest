#encodeing:utf-8
#!/usr/bin/python
#filename standard.py
import pickle as p
import os
class perpson:
    def __init__(self):
        self.info=[]
    def addUser(self,name,age,phone):
        saveFile = 'saveFile.data'
        tmp={'name':name,'age':age,'phone':phone}
        if(os.path.exists(saveFile)==False):
            f=file(saveFile,'w')
            self.info.append(tmp)
            p.dump(self.info, f)
            f.close()
            # print self.info
        else:
            f=file(saveFile)
            self.info = p.load(f)
            self.info.append(tmp)
            f.close()
            f=file(saveFile,'w')
            p.dump(self.info,f)
            f.close()
            # print self.info
        print 'add is success'
    def checkLook(self):
        saveFile = 'saveFile.data'
        if(os.path.exists(saveFile)==False):
            print 'file is not exsits'
        else:
            f = file(saveFile)
            info = p.load(f)
            f.close()
            print info
    def clearAll(self):
        if(os.path.exists('saveFile.data')==False):
            print 'the file is not exists'
        else:
            os.remove('saveFile.data')
            print 'remove is success'
    def __del__(self):
        del self.info

people = perpson()
# people.checkLook()
# people.clearAll()
people.addUser('zs','10',152424)

