#encoding: utf-8
#!/usr/bin/python
#Filename people.py
class people:
    def __init__(self,name):
        self.name=name
    def say(self):
        print self.name+": how are you "
    def eat(self):
        print self.name+" eat apple"


class student(people):
    def __init__(self,name):
        people.__init__(self,name)
        self.name=name
    def say(self):
        print self.name+": how old are you"
    def eat(self):
        print self.name+": eat banana"

    def parentsay(self):
        #people.say()
        pass
    def __setitem__(self, key, value):
        #self.data[key]=value
        pass



student = student('zx')
student.say()
student.parentsay()

people = people('zs')
people.say()
