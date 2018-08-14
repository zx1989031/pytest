#!/usr/bin/python
#Filename: backup_var1.py
import os
import time

#1.the file and directories to be backed up are specified in a list
source = [r'C:\Users\Administrator\Desktop\tmp']
target_dir = [r'D:\test']
print target_dir

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'



zip_command = " Info-Zip '%s' %s " % (target,' '.join(source))

if os.system(zip_command) ==0:
    print 'Successful backup to',target
else:
    print 'failed'