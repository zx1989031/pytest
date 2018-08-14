#!/usr/bin/python
# Filename:len.py
def __len__(string):
    val=0
    for i in string:
        val+=val
    return val+1



strings = " don't, world"

if (strings[-1]=='.') :
    # print strings[0].upper() + strings[1:]
    pass
else:
    pass
    # print strings[0].upper() + strings[1:]+'.'

# print strings[0].upper()+strings[1:-1]+(strings[-1]=='.' or '.')

import re
patten = "[a-zA-Z]+'?[a-z]?"
res = re.search(patten,strings)
print res.group()

text = 'find the river'
symbol='e'
num = 0
key = 0
tagkey = 0
for index in text:
    if (index == symbol):
        num = num + 1
    if (num == 2 and index == symbol):
        tagkey = key
    key = key + 1


if (num < 2 or tagkey == 0):
    print None
else:
    print tagkey
