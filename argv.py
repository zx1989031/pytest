#encoding: utf-8
#!/usr/bin/python
# argv.py
import sys
#sys.argv 本身当作 list 中的一个元素。获取外部元素后 多维数组依次将获取到的外部参数当做一个 list
argv = sys.argv[1][0]
print argv
