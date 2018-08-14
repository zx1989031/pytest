#coding:utf8
#/usr/bin/python
#fileName dostr.py
#a-z 97-122 A-Z 65-90

def checkio(world):
    asciiArr =[i for i in range(97,123,1)]
    letterList =[]
    for i in asciiArr:
        tmp = [i,0]
        for j in world:
            num = ord(str(j).lower())
            if num==i:
                tmp[1] = tmp[1]+1

        letterList.append(tmp)

    if (len(letterList) == 1):
        return chr(letterList[0][0])
    key =0
    for (x,y) in letterList:
        for j in range(1,len(letterList),1):
            tmp = letterList[key]
            if(letterList[key][1]<letterList[j][1]):
                letterList[key] = letterList[j]
                letterList[j] = tmp
            elif letterList[key][1]==letterList[j][1]:
                if(letterList[key][0]>letterList[j][0]):
                    letterList[key] = letterList[j]
                    letterList[key] = tmp
                else:
                    pass
            else:
                pass
        key=key+1
    return chr(letterList[0][0])

import string
def checkios(text):
    text = text.lower()

    return max(string.ascii_lowercase, key=text.count)

print checkios('adadfadxxxAAXX%')

# dlist = letterLen.items()
#letter = sorted(zip(letterLen.values(),letterLen.keys()))
#print letter[len(letter)-1]


