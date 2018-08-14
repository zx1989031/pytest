#coding:utf8
#!/usr/bin/python/
#fileName : regular.py 正则
import re
str = 'hello world'
print str.replace('hello','namehello')

pattern = re.compile(r"hello")
match = re.search(pattern,str)
print match.group(0)

# key = r"<html><body><h1>hello world<h1></body></html>"#这段是你要匹配的文本
# p1 = r"(?<=<h1>).+?(?=<h1>)"#这是我们写的正则表达式规则，你现在可以不理解啥意思
# pattern1 = re.compile(p1)#我们在编译这段正则表达式
# matcher1 = re.search(pattern1,key)#在源文本中搜索符合正则表达式的部分
# print matcher1.group(0)#打印出来

# key = r"javapythonhtmlvhdl"#这是源文本
# p1 = r"python"#这是我们写的正则表达式
# pattern1 = re.compile(p1)#同样是编译
# matcher1 = re.search(r"python",key)#同样是查询
# print matcher1.group(0)