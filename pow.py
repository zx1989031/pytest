#encodeing:utf-8
#!/usr/bin/python
#filename os.py

def powersum(power,*args):
    ''' return the sum of each '''
    total = 0
    for i in args:
        total +=pow(i,power)
    return total


print powersum(2,3,4)